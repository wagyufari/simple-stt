import os
import base64
import tempfile
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import shutil
import platform
from contextlib import asynccontextmanager

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

import mlx_whisper

# Check if ffmpeg is installed
if not shutil.which("ffmpeg"):
    # Common Homebrew path on Apple Silicon
    brew_ffmpeg_path = "/opt/homebrew/bin"
    if platform.system() == "Darwin" and os.path.exists(os.path.join(brew_ffmpeg_path, "ffmpeg")):
        os.environ["PATH"] += os.pathsep + brew_ffmpeg_path
        print(f"ℹ️ Added {brew_ffmpeg_path} to PATH to find ffmpeg.")
    else:
        print("❌ ERROR: 'ffmpeg' not found in PATH.")
        print("Please install FFmpeg to use this API:")
        print("  brew install ffmpeg")

MODEL_NAME = "mlx-community/whisper-large-v3-turbo"
MODEL_DIR = os.path.join(BASE_DIR, "models", "whisper-large-v3-turbo")

# Use local model dir if available, otherwise fallback to repo name
MODEL_PATH = MODEL_DIR if os.path.exists(MODEL_DIR) else MODEL_NAME

@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"Pre-caching model: {MODEL_PATH}...")
    # This will trigger a download if not already cached and load it into MLX memory
    # A dummy inference run can be slow the very first time on MLX since it compiles the computational graph!
    yield

app = FastAPI(title="MLX Whisper STT API", lifespan=lifespan)

class AudioRequest(BaseModel):
    audio_base64: str
    language: str = "auto"

class AudioResponse(BaseModel):
    text: str

@app.post("/transcribe", response_model=AudioResponse)
async def transcribe(req: AudioRequest):
    try:
        audio_data = base64.b64decode(req.audio_base64)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid base64 string provided.")
        
    tmp_path = None
    try:
        # Save to temp file; mlx-whisper uses ffmpeg to load audio
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(audio_data)
            tmp_path = tmp.name
            
        kwargs = {}
        if req.language and req.language.lower() != "auto":
            kwargs["language"] = req.language
            
        print(f"Transcribing {tmp_path} (language: {req.language})...")
        # Run transcription via MLX
        result = mlx_whisper.transcribe(
            tmp_path,
            path_or_hf_repo=MODEL_PATH,
            **kwargs
        )
        
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
            
        return AudioResponse(text=result.get("text", "").strip())
        
    except Exception as e:
        if tmp_path and os.path.exists(tmp_path):
            os.remove(tmp_path)
        print(f"Error during MLX transcription: {e}")
        raise HTTPException(status_code=500, detail=f"Transcription failed: {str(e)}")

@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "engine": "mlx-whisper",
        "model": MODEL_PATH
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=6684)


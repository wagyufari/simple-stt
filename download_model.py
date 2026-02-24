import os
from huggingface_hub import snapshot_download

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_NAME = "mlx-community/whisper-large-v3-turbo"
MODEL_DIR = os.path.join(BASE_DIR, "models", "whisper-large-v3-turbo")

def download():
    print(f"Downloading {MODEL_NAME} to {MODEL_DIR}...")
    snapshot_download(
        repo_id=MODEL_NAME,
        local_dir=MODEL_DIR,
        local_dir_use_symlinks=False
    )
    print("\n✅ Model downloaded successfully!")

if __name__ == "__main__":
    download()

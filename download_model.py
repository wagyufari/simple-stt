import os
from huggingface_hub import snapshot_download

# Redirect Hugging Face cache to the project directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.environ["HF_HOME"] = os.path.join(BASE_DIR, "models")

MODEL_NAME = "mlx-community/whisper-large-v3-turbo"

def download():
    print(f"Downloading {MODEL_NAME} to local models directory...")
    snapshot_download(repo_id=MODEL_NAME)
    print("\n✅ Model downloaded successfully!")

if __name__ == "__main__":
    download()

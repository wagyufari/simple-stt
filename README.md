# 🎙️ Simple STT (MLX Whisper)

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-macOS%20(Apple%20Silicon)-lightgrey.svg)](https://developer.apple.com/apple-silicon/)
[![Engine](https://img.shields.io/badge/Engine-MLX%20Whisper-orange.svg)](https://github.com/ml-explore/mlx-whisper)

A high-performance, lightweight **Speech-to-Text API** specifically engineered for **Apple Silicon Macs** (M1, M2, M3, M4). By leveraging the [MLX framework](https://github.com/ml-explore/mlx), this project provides near-instant audio transcription with full hardware acceleration and minimal memory footprint.

---

## ✨ Key Features

- 🍎 **Apple Silicon Optimized**: Fully utilizes the GPU/Neural Engine via the MLX framework for maximum throughput.
- ⚡ **Turbo Performance**: Defaults to the `whisper-large-v3-turbo` model for a perfect balance of speed and accuracy.
- 🛠️ **Developer Friendly**: Simple REST API built with FastAPI, making it easy to integrate into any application.
- 📦 **Zero-Configuration Model Management**: Automatically downloads and manages models locally within the project directory.
- 🔇 **Privacy Focused**: Runs 100% locally on your machine. No data ever leaves your computer.

---

## 🚀 Getting Started

### Initial Setup

Copy and paste the following block to install dependencies, set up the environment, and download the model:

```bash
# 1. Clone the repository
git clone https://github.com/wagyufari/simple-stt.git
cd simple-stt

# 2. Run the automated setup script
# This script installs FFmpeg, creates a virtual environment, 
# installs dependencies, and downloads the Whisper model.
chmod +x setup.sh
./setup.sh
```

---

## 🏃 Running the Server

### Standard Mode
Runs the server in the foreground on `http://localhost:6684`.
```bash
python main.py
```

### Background Mode (Recommended for production)
Runs the server in the background and logs to `api.log`.
```bash
nohup ./venv/bin/python main.py > api.log 2>&1 &
```

---

## 📖 API Usage

The server exposes a `/transcribe` endpoint that accepts base64-encoded audio.

### Example Request (cURL)

```bash
curl -X POST http://localhost:6684/transcribe \
     -H "Content-Type: application/json" \
     -d '{
       "audio_base64": "'"$(base64 -i your_audio.wav)"'",
       "language": "en"
     }'
```

For detailed documentation on all endpoints and response formats, see [**API.md**](./API.md) or visit the interactive documentation at `http://localhost:6684/docs` when the server is running.

---

## 🛠️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **ML Engine**: [MLX Whisper](https://github.com/ml-explore/mlx-whisper)
- **Audio Processing**: [FFmpeg](https://ffmpeg.org/)
- **Schema Validation**: [Pydantic](https://docs.pydantic.dev/)

---

## 📁 Project Structure

- `main.py`: The core FastAPI application and transcription logic.
- `setup.sh`: Automated environment setup script.
- `download_model.py`: Utility to pre-download models from Hugging Face.
- `API.md`: Detailed API endpoint documentation.
- `models/`: (Generated) Local storage for downloaded MLX models.

---

## 📝 License

This project is open-source and available under the MIT License.


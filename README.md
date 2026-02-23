# 🎙️ Simple STT (MLX Whisper)

A high-performance, lightweight Speech-to-Text API built for Apple Silicon Mac (M-series). It utilizes `mlx-whisper` and FastAPI to provide rapid audio transcription with hardware acceleration.

## ✨ Features

- **Apple Silicon Optimized**: Uses the MLX framework for maximum performance on M1/M2/M3/M4 chips.
- **Turbo Speed**: Uses the `large-v3-turbo` model for a great balance of accuracy and speed.
- **Self-Contained**: Automatically downloads and stores models inside the project directory.

## 🚀 Quick Start

### 1. Prerequisites

- **Python 3.10+**
- **FFmpeg** (Required for audio processing): `brew install ffmpeg`

### 2. Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd simple-stt

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Running the Server

**Standard Start:**

```bash
python main.py
```

**Background Start:**

```bash
nohup ./venv/bin/python main.py > api.log 2>&1 &
```

## 📖 API Documentation

Detailed endpoint documentation can be found in [API.md](./API.md).

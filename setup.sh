#!/bin/bash

# Exit on error
set -e

echo "🚀 Setting up Simple STT..."

# 1. Check for Homebrew
if ! command -v brew &> /dev/null; then
    echo "❌ Homebrew not found. Please install it from https://brew.sh/"
    exit 1
fi

# 2. Check for FFmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "📦 Installing FFmpeg via Homebrew..."
    brew install ffmpeg
else
    echo "✅ FFmpeg is already installed."
fi

# 3. Create Virtual Environment
if [ ! -d "venv" ]; then
    echo "🐍 Creating virtual environment..."
    python3 -m venv venv
else
    echo "✅ Virtual environment already exists."
fi

# 4. Install Python Dependencies
echo "📥 Installing Python dependencies..."
./venv/bin/pip install --upgrade pip
./venv/bin/pip install -r requirements.txt

# 5. Download Whisper Model
echo "🤖 Downloading Whisper model (large-v3-turbo)..."
./venv/bin/python download_model.py

echo "✅ Setup complete! You can now start the server with './venv/bin/python main.py'"

# 📖 API Documentation

The STT Server runs by default on `http://localhost:6684`.

## Endpoints

### 1. Transcribe Audio

**`POST /transcribe`**

Converts base64 encoded audio into text.

**Request Body:**

```json
{
  "audio_base64": "UklGRi...",
  "language": "auto"
}
```

- `audio_base64`: String. The raw audio file (WAV, MP3, etc.) encoded in Base64.
- `language`: String (optional). The ISO language code (e.g., "en", "es", "fr"). Defaults to `"auto"` for automatic detection.

**Response Body:**

```json
{
  "text": "The transcribed text here."
}
```

---

### 2. Health Check

**`GET /health`**

Check if the server is running and which model is currently loaded.

**Response Body:**

```json
{
  "status": "ok",
  "engine": "mlx-whisper",
  "model": "mlx-community/whisper-large-v3-turbo"
}
```

## Example Usage (cURL)

```bash
curl -X POST http://localhost:6684/transcribe \
     -H "Content-Type: application/json" \
     -d '{
       "audio_base64": "'"$(base64 -i your_audio.wav)"'",
       "language": "en"
     }'
```

## Interactive Docs

When the server is running, you can access the interactive Swagger UI at:
[http://localhost:6684/docs](http://localhost:6684/docs)

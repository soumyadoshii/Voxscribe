# Voxscribe - AI Voice Cloner 🎤

Voxscribe lets you clone your voice using AI! Upload a WAV sample of your voice, type any text, and get a generated audio in your own voice.

## 🚀 Features

- Upload a `.wav` audio sample.
- Enter any text to generate your voice clone.
- Play the generated audio directly in the browser.
- Simple, modern, and interactive UI.

---

## 💻 How to Use

1. Open the app in your browser.
2. Upload your WAV voice sample.
3. Enter the text you want to clone.
4. Click **Generate Voice**.
5. Listen to your cloned voice in the audio player.

---

## 🛠 Tech Stack

- Frontend: HTML, CSS, JavaScript  
- Backend: Python, Flask  
- TTS Engine: Coqui AI TTS ([GitHub](https://github.com/coqui-ai/TTS))  

---

## ⚡ Run Locally

```bash
git clone https://github.com/yourusername/voicecloner.git
cd voicecloner
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python app.py

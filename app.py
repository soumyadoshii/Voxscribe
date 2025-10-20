from flask import Flask, request, send_file
import os
from main import generate_audio  # Import function from main.py

app = Flask(__name__)

@app.route('/')
def index():
    # Serve the main HTML interface
    return send_file('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form.get('text')
    voice_file = request.files.get('voice')

    if not text or not voice_file:
        return "Text or voice file missing", 400

    # Save uploaded voice sample
    os.makedirs("voice_samples", exist_ok=True)
    voice_path = os.path.join("voice_samples", "user.wav")
    voice_file.save(voice_path)

    # Run your voice cloning logic
    output_path = generate_audio(text, voice_path)

    # Send back the generated audio file
    return send_file(output_path, mimetype='audio/wav')

if __name__ == "__main__":
    app.run(debug=True)

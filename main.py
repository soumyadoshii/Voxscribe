import os
from TTS.api import TTS

def generate_audio(text_to_speak, voice_sample_path):
    """Generates a cloned voice saying the input text."""
    output_file = "outputs/output.wav"
    os.makedirs("outputs", exist_ok=True)

    # Load the multilingual YourTTS model
    tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts")

    # Generate the cloned voice
    tts.tts_to_file(
        text=text_to_speak,
        speaker_wav=voice_sample_path,
        file_path=output_file,
        language="en"
    )

    print(f"✅ Voice cloned successfully! Saved at: {output_file}")
    return output_file

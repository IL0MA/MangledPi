import os

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play

load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")

if not api_key:
    raise RuntimeError("ELEVENLABS_API_KEY was not found in the .env file.")

client = ElevenLabs(api_key=api_key)

print("Sending text to ElevenLabs...")

audio = client.text_to_speech.convert(
    text="Crash detected. Are you okay?",
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_v3",
    output_format="mp3_44100_128",
)

print("Playing audio...")

play(audio)

print("Done.")
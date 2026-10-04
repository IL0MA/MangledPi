import os
import time

from flask import Flask
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play

load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")

if not api_key:
    raise RuntimeError("ELEVENLABS_API_KEY not found in .env")

client = ElevenLabs(api_key=api_key)

app = Flask(__name__)

# Prevent the webpage from triggering the voice repeatedly
last_crash_time = 0
COOLDOWN_SECONDS = 10


def say_crash_message():
    print("CRASH DETECTED!")

    audio = client.text_to_speech.convert(
        text="Crash detected. Are you okay?",
        voice_id="JBFqnCBsd6RMkjVDRZzb",
        model_id="eleven_v3",
        output_format="mp3_44100_128",
    )

    play(audio)


@app.route("/crash", methods=["POST", "GET"])
def crash():
    global last_crash_time

    current_time = time.time()

    if current_time - last_crash_time < COOLDOWN_SECONDS:
        print("Crash trigger ignored - cooldown active.")
        return "COOLDOWN", 200

    last_crash_time = current_time

    say_crash_message()

    return "CRASH RECEIVED", 200


@app.route("/", methods=["GET"])
def home():
    return "Crash detection server is running.", 200


if __name__ == "__main__":
    print("Crash server running...")
    print("Waiting for crash detection from ST AIoT Craft...")
    app.run(host="127.0.0.1", port=5000)
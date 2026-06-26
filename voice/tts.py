from elevenlabs.client import ElevenLabs

from elevenlabs.play import play
from config import eapi_key
import datetime

client = ElevenLabs(api_key=eapi_key)


def speak(text):

    try:

        audio = client.text_to_speech.convert(
            text=text,
            voice_id="pNInz6obpgDQGcFmaJgB",
            model_id="eleven_multilingual_v2"
        )

        play(audio)

    except Exception as e:

        print("ElevenLabs Error:", e)

def wishme():
    hour =int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("GOOD MORNING Sir, Greetings ,How may I help you ? ")
       
    elif hour >= 12 and hour < 18:
        speak("GOOD AFTERNOON Sir, Greetings ,How may I help you ? ")
       
    elif hour >= 18 and hour < 21:
        speak("GOOD evening Sir, Greetings ,How may I help you ? ")
       
    else:
        speak("GOOD NIGHT Sir, Greetings ,How may I help you ? ")

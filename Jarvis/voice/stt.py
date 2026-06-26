from faster_whisper import WhisperModel
import sounddevice as sd
from scipy.io.wavfile import write




# Load Whisper model once
model = WhisperModel("base", compute_type="int8")

# All the functions are defined here

def takecommands():
    global model

    if model is None:
        print("Loading Whisper...")
        model = WhisperModel("tiny", compute_type="int8")

    try:

        fs = 16000
        seconds = 5

        print("Listening...")

        recording = sd.rec(
            int(seconds * fs),
            samplerate=fs,
            channels=1,
            dtype='int16'
        )

        sd.wait()

        # print("Recording complete")

        write("input.wav", fs, recording)
        print("Recognizing...")

        segments, info = model.transcribe(
        "input.wav",
        language='en',
        beam_size=5,
        vad_filter=True
        )

        query = ""

        for segment in segments:
            query += segment.text

        query = query.lower().strip()

        print(f"User said: {query}")

        return query

    except Exception as e:

        print("Whisper Error:", e)

        return ""
        

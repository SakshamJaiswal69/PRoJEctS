# All the imports
from voice.stt import takecommands
from voice.tts import speak, wishme


def wakeup():
    wake_words = ["jarvis", "wake up", "hello jarvis"]
    while True:
    
        print("Sleeping...")

        query = takecommands()

        if not query:
            continue

        query = query.lower()

        if any(word in query for word in wake_words):

            speak("Yes sir.")
            wishme()

            break


from voice.wakeup import wakeup
from voice.stt import takecommands
from voice.tts import speak, wishme
from core.tools import process_command
from memory.initialize_memory import initialize_memory
import time

if __name__ == "__main__":
    # speak("Initializing JARVIS...")
    print("Initializing JARVIS...")

    initialize_memory()

    while True:

        wakeup()

        while True:

            query = takecommands()

            
            # if not query.startswith("jarvis"):
            #     continue
            if not query:
                continue
            # query = query.replace("jarvis", "", 1).strip()
            # query = query.lower()
            # time.sleep(1)

            process_command(query)

            time.sleep(1)
# All the imports
from faster_whisper import WhisperModel
import sounddevice as sd
from scipy.io.wavfile import write
import datetime
import wikipedia
import webbrowser
import os
import time
import smtplib
import openai
import sqlite3
# import threading
from config import API


is_speaking = False
speech_thread = None
chatStr=""
# Load Whisper model once
model = WhisperModel("base", compute_type="int8")

# All the functions are defined here

from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
from config import eapi_key

client = ElevenLabs(
    api_key=eapi_key
)
# def speak(text):

#     global is_speaking

#     def run_speech():

#         global is_speaking

#         try:

#             is_speaking = True

#             audio = client.text_to_speech.convert(
#                 text=text,
#                 voice_id="pNInz6obpgDQGcFmaJgB",
#                 model_id="eleven_multilingual_v2"
#             )

#             play(audio)

#         except Exception as e:

#             print("ElevenLabs Error:", e)

#         finally:

#             is_speaking = False

#     threading.Thread(
#         target=run_speech,
#         daemon=True
#     ).start()
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

# def stop_speaking():

#     interrupt_words = ["stop","jarvis stop","wait","be quiet"]
#     if any(word in query for word in interrupt_words):
#         print("Interrupt detected")


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
        
def takecommands():
    global model

    if model is None:
        print("Loading Whisper...")
        model = WhisperModel("tiny", compute_type="int8")

    try:

        fs = 16000
        seconds = 7

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

        if len(query) < 3:
            return ""

        print(f"User said: {query}")

        return query

    except Exception as e:

        print("Whisper Error:", e)

        return ""

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("saksham69jaiswal@gmail.com", "Password")
    server.sendmail("saksham69jaiswal@gmail.com", to, content)
    server.quit()

def ask_ai(prompt):
    from openai import OpenAI

    client =OpenAI(api_key = API)
    response = client.responses.create(
        model="gpt-5.4-mini",
        input=prompt,
        store=True,
    )

    print(response.output_text);

    # # Create folder if not exists
    # if not os.path.exists("OpenAI_Responses"):
    #     os.mkdir("OpenAI_Responses")

    # # Create safe filename
    # filename = prompt.replace(" ", "_")[:30]

    # # Save response
    # with open(f"OpenAI_Responses/{filename}.txt", "w", encoding="utf-8") as f:

    #     f.write(f"Prompt:\n{prompt}\n\n")

    #     f.write(f"Response:\n{response.output_text}\n")

        
    
    speak(response.output_text);



def chat(query):

    from openai import OpenAI

    global chatStr

    client = OpenAI(api_key=API)

    memory_info = get_all_memories()
    full_prompt = f"""

                Known memory:
                {memory_info}

                Conversation:
                {chatStr}

                User: {query}
                """
    

    # Add user message

    # Prevent huge memory
    chatStr = chatStr[-4000:]
    # conversation_history = []

    response = client.responses.create(
        model="gpt-5.4-mini",
        input=full_prompt,
        store=True,
    )

    reply = response.output_text

    chatStr += f"Saksham: {query}\n"
    chatStr += f"Jarvis: {reply}\n"

    print(reply)

    speak(reply)

    # Save response in memory
    # chatStr += f"{reply}\n"

    return reply

def wakeup():

    wake_words = ["jarvis", "wake up", "hello jarvis"]

    while True:
    
        print("Sleeping...")

        query = takecommands()

        if not query:
            continue

        query = query.lower()

        if any(word in query for word in wake_words):

            # speak("Yes sir.")
            wishme()

            break
def initialize_memory():

    conn = sqlite3.connect("memory.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memories (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        category TEXT,

        key TEXT,

        value TEXT,

        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()

    conn.close()

def remember(category, key, value):

    conn = sqlite3.connect("memory.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM memories WHERE key=?",
        (key,)
    )

    existing = cursor.fetchone()

    if existing:

        cursor.execute(
            """
            UPDATE memories
            SET value=?
            WHERE key=?
            """,
            (value, key)
        )

    else:

        cursor.execute(
            """
            INSERT INTO memories
            (category, key, value)

            VALUES (?, ?, ?)
            """,
            (category, key, value)
        )

    conn.commit()

    conn.close()

    speak(f"I will remember that {key} is {value}")

def recall(key):

    conn = sqlite3.connect("memory.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT value
        FROM memories
        WHERE key=?
        ORDER BY id DESC
        LIMIT 1
        """,
        (key,)
    )

    result = cursor.fetchone()

    conn.close()

    if result:

        return result[0]

    return "I do not remember that yet."


def get_all_memories():

    conn = sqlite3.connect("memory.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT key, value FROM memories
    ORDER BY id DESC
    LIMIT 20
    """)

    memories = cursor.fetchall()

    conn.close()

    memory_text = ""

    for key, value in memories:
        memory_text += f"{key}: {value}\n"

    return memory_text

# Main function    

if __name__ == "__main__":
    initialize_memory()

    while True:

        # WAIT FOR WAKE WORD
        wakeup()

        

        # speak("Jarvis activated sir.")

        active = True

        # CONTINUOUS CONVERSATION LOOP
        while active:

            query = takecommands()

            if not query:
                continue

            # elif not query.startswith("jarvis"):
            #     continue

            query = query.replace("jarvis", "", 1).strip()
            query = query.lower()
            time.sleep(1)
            # logics for excecuting tasks 
            if 'wikipedia' in query:
                speak("Searching Wikipedia ...")
                
                query = query.replace("wikipedia", "")
                
                results = wikipedia.summary(query,sentences=3)
                speak("According to WikiPedia,")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
            
            elif 'open google' in query:
                webbrowser.open("google.com")
            
            # elif 'play music' in query:
            #     music_dir = "C:\\Users\\Ayush\\Music"
            #     songs = os.listdir(music_dir)
            #     print(songs)
            #     os.startfile(os.path.join(music_dir, songs[0]))
            
            elif 'open friend' in query:
                webbrowser.open("chatgpt.com")

            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"Sir, the time is {strTime}")
                speak(f"Sir, the time is {strTime}")
            
            elif 'open code editor' in query:
                codePath = "C:\\Users\\A6136\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'open whatsapp' in query:
                whatsappPath = "C:\\Users\\A6136\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                os.startfile(whatsappPath)

            elif "send an email" in query:
                try:
                    speak("What should I say ?")
                    content = takecommands()
                    to = "saksham69jaiswal@gmail.com"
                    sendEmail(to,content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("Sorry Sir, I am not able to send this email !")

            elif "ai" in query:

                speak("AI mode activated sir.")
                ai_mode = True

                while ai_mode:

                    speak("What is your query?")
                    query = takecommands()

                    if not query:
                        continue

                    query = query.lower()

                    if query in ["stop", "exit", "quit", "bye", "close ai"]:
                        speak("Exiting AI mode sir.")
                        ai_mode = False
                        break

                    ask_ai(query)

            elif "show all memories" in query:

                memories = get_all_memories()

                print(memories)

                speak("Here are your stored memories.")

            elif "remember" in query:

                speak("What should I remember?")

                data = takecommands()

                

                if " is " in data:

                    key, value = data.split(" is ", 1)

                    key = key.strip()

                    value = value.strip()

                    remember(
                        "general",
                        key,
                        value
                    )

                else:

                    speak("Please say it in proper format.")


            elif "what do you know about" in query:

                key = query.replace(
                    "what do you know about",
                    ""
                ).strip()

                result = recall(key)

                speak(result)
        
            elif "shut down" in query or "Shut down" in query or "exit" in query or "Exit" in query or"shutdown" in query or "Shutdown" in query:
                speak("Shutting down, Goodbye Sir!")
                exit()


            elif "reset" in query:
                speak("Resetting, Just a moment Sir!")
                chatStr = ""

#             elif any(word in query for word in [
#     "wait",
#     "stop talking",
#     "be quiet",
#     "silence"
# ]):
#                 stop_speaking()

#                 continue
            else :
                chat(query)
                
                
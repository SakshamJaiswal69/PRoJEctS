import datetime
import wikipedia
import webbrowser
import os
import smtplib

from voice.tts import speak
from voice.stt import takecommands
from core.brain import chat, ask_ai
from memory.remember import remember
from memory.recall import recall
from memory.getallmemo import get_all_memories






def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("saksham69jaiswal@gmail.com", "Password")
    server.sendmail("saksham69jaiswal@gmail.com", to, content)
    server.quit()


def process_command(query):
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
        
    elif "shut down" in query or "Shut down" in query :
            speak("Shutting down, Goodbye Sir!")
            print("Shutting down, Goodbye Sir!")
            exit()


    elif "reset" in query:
            speak("Resetting, Just a moment Sir!")
            chatStr = ""

#   elif any(word in query for word in [
#     "wait",
#     "stop talking",
#     "be quiet",
#     "silence"
#       ]):
#                 stop_speaking()

#                 continue
    else :
        chat(query)
                
                   
            
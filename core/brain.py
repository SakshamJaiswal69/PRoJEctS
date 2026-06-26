
import datetime
import wikipedia
import webbrowser
import os
import time
import smtplib

from voice.tts import speak
from voice.stt import takecommands
import openai
from config import API
from memory.remember import remember
from memory.recall import recall
from memory.getallmemo import get_all_memories
from memory.initialize_memory import initialize_memory

chatStr = ""



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

# def process_command(query):
#     # if not query.startswith("jarvis"):
#     #     return

#     # query = query.replace("jarvis", "", 1).strip()
#     # query = query.lower()
#     # time.sleep(1)

#     # if "open" in query:
#     #     open_app(query)
#     # elif "search" in query:
#     #     search_web(query)
#     # elif "play" in query:
#     #     play_music(query)
#     # elif "time" in query:
#     #     tell_time()
#     # elif "date" in query:
#     #     tell_date()
#     # elif "weather" in query:
#     #     get_weather(query)
#     # elif "news" in query:
#     #     get_news()
#     # elif "joke" in query:
#     #     tell_joke()
#     # elif "quote" in query:
#     #     tell_quote()
#     # elif "reminder" in query:
#     #     set_reminder(query)
#     # elif "alarm" in query:
#     #     set_alarm(query)
#     # elif "email" in query:
#     #     send_email(query)
#     # else:
#     #     chat(query)
#         # logics for excecuting tasks 
#             if 'wikipedia' in query:
#                 speak("Searching Wikipedia ...")
                
#                 query = query.replace("wikipedia", "")
                
#                 results = wikipedia.summary(query,sentences=3)
#                 speak("According to WikiPedia,")
#                 print(results)
#                 speak(results)

#             elif 'open youtube' in query:
#                 webbrowser.open("youtube.com")
            
#             elif 'open google' in query:
#                 webbrowser.open("google.com")
            
#             # elif 'play music' in query:
#             #     music_dir = "C:\\Users\\Ayush\\Music"
#             #     songs = os.listdir(music_dir)
#             #     print(songs)
#             #     os.startfile(os.path.join(music_dir, songs[0]))
            
#             elif 'open friend' in query:
#                 webbrowser.open("chatgpt.com")

#             elif 'time' in query:
#                 strTime = datetime.datetime.now().strftime("%H:%M:%S")
#                 print(f"Sir, the time is {strTime}")
#                 speak(f"Sir, the time is {strTime}")
            
#             elif 'open code editor' in query:
#                 codePath = "C:\\Users\\A6136\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
#                 os.startfile(codePath)

#             elif 'open whatsapp' in query:
#                 whatsappPath = "C:\\Users\\A6136\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
#                 os.startfile(whatsappPath)

#             elif "send an email" in query:
#                 try:
#                     speak("What should I say ?")
#                     content = takecommands()
#                     to = "saksham69jaiswal@gmail.com"
#                     sendEmail(to,content)
#                     speak("Email has been sent !")
#                 except Exception as e:
#                     print(e)
#                     speak("Sorry Sir, I am not able to send this email !")

#             elif "ai" in query:

#                 speak("AI mode activated sir.")
#                 ai_mode = True

#                 while ai_mode:

#                     speak("What is your query?")
#                     query = takecommands()

#                     if not query:
#                         continue

#                     query = query.lower()

#                     if query in ["stop", "exit", "quit", "bye", "close ai"]:
#                         speak("Exiting AI mode sir.")
#                         ai_mode = False
#                         break

#                     ask_ai(query)

#             elif "show all memories" in query:

#                 memories = get_all_memories()

#                 print(memories)

#                 speak("Here are your stored memories.")

#             elif "remember" in query:

#                 speak("What should I remember?")

#                 data = takecommands()

                

#                 if " is " in data:

#                     key, value = data.split(" is ", 1)

#                     key = key.strip()

#                     value = value.strip()

#                     remember(
#                         "general",
#                         key,
#                         value
#                     )

#                 else:

#                     speak("Please say it in proper format.")


#             elif "what do you know about" in query:

#                 key = query.replace(
#                     "what do you know about",
#                     ""
#                 ).strip()

#                 result = recall(key)

#                 speak(result)
        
#             elif "shut down" in query or "Shut down" in query :
#                 speak("Shutting down, Goodbye Sir!")
#                 exit()


#             elif "reset" in query:
#                 speak("Resetting, Just a moment Sir!")
#                 chatStr = ""

#             else:
#                 chat(query)
                
# All the imports
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import openai
from config import API
# from config import password
chatStr=""
# All the functions are defined here

def speak(audio):

    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[0].id)

    engine.setProperty('rate', 200)

    engine.say(str(audio))

    engine.runAndWait()

    engine.stop()

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
    # it takes mic input and return sting as voice
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listing...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("recognizing...")
        query =r.recognize_google(audio,language ='en-in')
        print(f"user said : {query}\n")

    except Exception as e:
        # print(e) 
        print("Say that Again Please ...")
        return "None"
    return query

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
    # client = OpenAI(
    #     api_key="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"
    # )

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

    # Add user message
    chatStr += f"Saksham : {query}\nJarvis: "

    # Prevent huge memory
    chatStr = chatStr[-4000:]

    response = client.responses.create(
        model="gpt-5.4-mini",
        input=chatStr,
        store=True,
    )

    reply = response.output_text

    print(reply)

    speak(reply)

    # Save response in memory
    chatStr += f"{reply}\n"

    return reply

def wakeup():

    wake_words = ["jarvis", "wake up", "hello jarvis"]

    # while True:
    if 1:
        print("Sleeping...")


        query = takecommands().lower()

        if any(word in query for word in wake_words):

            
            wishme()

            # break
# Main function    

if __name__ == "__main__":

    # wishme()
    while True :
        wakeup()
    # if 1:
        query = takecommands().lower()
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

        elif 'the time' in query:
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
                prompt = takecommands()

                if prompt == "None":
                    continue

                prompt = prompt.lower()

                if prompt in ["stop", "exit", "quit", "bye", "close ai"]:
                    speak("Exiting AI mode sir.")
                    ai_mode = False
                    break

                ask_ai(prompt)


       
        elif "shutdown" in query or "Shut down" in query or "sleep" in query or "go to sleep" in query:
            speak("Shutting down, Goodbye Sir!")
            exit()


        elif "reset" in query:
            speak("Resetting, Just a moment Sir!")
            chatStr = ""


        else :
            chat(query)
            
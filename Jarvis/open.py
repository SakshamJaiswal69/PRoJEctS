from openai import OpenAI

client = OpenAI(
  api_key="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"
)

response = client.responses.create(
  model="gpt-5.4-mini",
  input="who is Iron Man ?",
  store=True,
)

print(response.output_text);
'''
 **Real name:** Tony Stark  
- **First appearance:** *Tales of Suspense* #39 (1963)  
- **Created by:** Stan Lee, Larry Lieber, Don Heck, and Jack Kirby  
- **Powers:** No natural superpowers; he relies on his intelligence and powered armor  

In the Marvel movies, Iron Man is played by **Robert Downey Jr.**
'''elif "ai" in query.lower():

    speak("AI mode activated sir.")

    ai_mode = True

    while ai_mode:

        speak("What is your query?")
        prompt = takecommands().lower()

        if "stop" in prompt or "exit" in prompt:
            speak("Exiting AI mode sir.")
            ai_mode = False
            continue

        ask_ai(prompt)
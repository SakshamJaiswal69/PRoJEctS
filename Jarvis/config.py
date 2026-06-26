Email="A6136593@gmail.com"
Password="SAKSHAM@#69"
API = "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"

# from openai import OpenAI

# client = OpenAI(
#   api_key="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"
# )

# response = client.responses.create(
#   model="gpt-5.4-mini",
#   input="write a haiku about ai",
#   store=True,
# )

# print(response.output_text);
eapi_key = "sk_d57ccf7909f50a0690672dc7d1b0a0325d7ec28ec1464bf5"
# sk_d57ccf7909f50a0690672dc7d1b0a0325d7ec28ec1464bf5
def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('ai')[1:]).strip() }.txt", "w") as f:
        f.write(text)

        '''
        # Load Whisper model once
model = WhisperModel("base", compute_type="int8")

def takecommands():

    fs = 44100
    seconds = 5

    print("Listening...")

    recording = sd.rec(
        int(seconds * fs),
        samplerate=fs,
        channels=1
    )

    sd.wait()

    write("input.wav", fs, recording)

    print("Recognizing...")

    segments, info = model.transcribe("input.wav")

    query = ""

    for segment in segments:
        query += segment.text

    query = query.lower()

    print(f"User said: {query}")

    return query'''
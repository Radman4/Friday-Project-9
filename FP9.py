import tkinter as ttk
import openai
import dotenv 
import os
apikey = os.getenv("personalkey")
#setup openai (will need to prchase tokens, i think)
client = openai.OpenAI(
    api_key=apikey
)

promptWindow = ttk()

class prompt:
    def __init__(self, master):
        frame1 = ttk.Frame(master, height = 200, width=300)
        frame1.pack()
    #textbox for the prompt
        self.promptText = ttk.Label(frame1, text ="Enter your prompt here")
        self.prompt = ttk.Entry(frame1)
        self.button1 = ttk.Button(frame1, text="Submit Prompt")
        self.button1.config(command=self.promptAnswer)
        #now to get ChatGPT to actually use the prompt!
    def promptAnswer(self):
        client = openai.OpenAI(
        api_key=apikey
    )
    response = client.responses.create(
    model="gpt-4.1",
    input=[
        {"role": "user", "content": "what teams are playing in this image?"},
        {"role": "user","content": [{"type": "input_text",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/3b/LeBron_James_Layup_%28Cleveland_vs_Brooklyn_2018%29.jpg"}]}])

    print(response.output_text)


    
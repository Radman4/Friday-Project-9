import tkinter as ttk
import openai
import dotenv
import os
apikey = os.getenv("personalkey.env")
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
        
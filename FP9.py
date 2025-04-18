
from tkinter import *
from tkinter import ttk
import openai
from dotenv import load_dotenv
import os
apikey = os.getenv("key")
#setup openai (will need to purchase tokens, i think)
openai.api_key = apikey
root = Tk()

class prompt:
    def __init__(self, master):
        frame1 = ttk.Frame(master, height = 200, width=300)
        frame1.pack(padx=10, pady=10)
    #textbox for the prompt
        self.promptText = ttk.Label(frame1, text ="Enter your prompt here")
        self.promptText.grid(column= 0, row= 0)
        self.prompt = ttk.Entry(frame1)
        self.prompt.grid(column= 0, row= 1)
        self.button1 = ttk.Button(frame1, text="Submit Prompt")
        self.button1.config(command=self.promptAnswer)
        self.button1.grid(column= 0, row= 2)
        #now to get ChatGPT to actually use the prompt!
    def promptAnswer(self):
            #  new window for output
        outputText = ttk.Frame(outputWindow, height=15, width=60)
        outputText.pack(padx=10, pady=10)
        outputWindow = ttk.Label(outputText, answer)

        try:
            # writing to chat GPT to tell it that  
            response = openai.ChatCompletion.create(
                model="gpt-4.1",  
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},])
        # Extract ChatGPT's response
            answer = response.choices[0].message.content.strip()
        except Exception as e:
            answer = f"An error occurred: {e}"


    

app = prompt(root)
root.mainloop()

    
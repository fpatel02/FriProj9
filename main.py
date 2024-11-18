import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import openai
from dotenv import load_dotenv
import os
#setting up OpenAI API key
apikey = os.getenv("key")

# Loading environment variables (key) from .env file
load_dotenv()
openai.api_key = os.getenv("key")

def get_completion():
    prompt = prompt_entry.get("1.0", tk.END).strip()
    if not prompt:
        messagebox.showerror("Error", "Please enter a prompt.")
        return
    try:
        response = open.ai.Completion.create(
            model = "text-davinci-003",
            prompt = prompt,
            max_tokens = 150
        )

        output_box.config(state = tk.NORMAL)
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, response.choices[0].text.strip())
        output_box.config(state = tk.DISABLED)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

#create main window
root = Tk()
root.title("OpenAI Completion GUI")

#prompt input area
prompt_label = tk.Label(root, text = "Enter your prompt:")
prompt_label.pack(pady = 10)

prompt_entry = tk.Text(root, height = 6, width = 50)
prompt_entry.pack(pady = 10)

#submit button
submit_button = tk.Button(root, text = "Submit", command = (get_completion))
submit_button.pack(pady = 10)

#output area
output_label = tk.Label(root, text = "Output:")
output_label.pack(pady = 10)

output_box = tk.Text(root, height = 10, width = 50, wrap = tk.WORD, state = tk.DISABLED)
output_box.pack(pady = 10)

root.mainloop()
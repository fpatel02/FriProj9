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

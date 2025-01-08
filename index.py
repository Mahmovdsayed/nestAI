import tkinter as tk
from tkinter import font
from meta_ai_api import MetaAI

ai = MetaAI()

def send_message(event=None):
    message = user_input.get()
    if message:
        try:
            chat_history.config(state=tk.NORMAL)
            chat_history.insert(tk.END, f"You: {message}\nNEST AI: Loading...\n\n")
            chat_history.config(state=tk.DISABLED)
            chat_history.see(tk.END)
            
            user_input.delete(0, tk.END)

           
            window.update_idletasks()  
            response = ai.prompt(message=message)  
            reply = response.get('message', 'Sorry, no response received.')
            
            chat_history.config(state=tk.NORMAL)
            chat_history.delete("end-3l", "end-1l")  
            chat_history.insert(tk.END, f"NEST AI: {reply}\n\n")
            chat_history.config(state=tk.DISABLED)
        except Exception as e:
            chat_history.config(state=tk.NORMAL)
            chat_history.insert(tk.END, f"Error: {e}\n\n")
            chat_history.config(state=tk.DISABLED)

window = tk.Tk()
window.title("NEST AI Chat")

custom_font = font.Font(family="Arial", size=12)

chat_history = tk.Text(window, state=tk.DISABLED, wrap=tk.WORD, width=50, height=20, font=custom_font)
chat_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

user_input = tk.Entry(window, width=40, font=custom_font)
user_input.grid(row=1, column=0, padx=10, pady=10)
user_input.bind("<Return>", send_message) 

send_button = tk.Button(window, text="Send", command=send_message, font=custom_font)
send_button.grid(row=1, column=1, padx=10, pady=10)

window.mainloop()

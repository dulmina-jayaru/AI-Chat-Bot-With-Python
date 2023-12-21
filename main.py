from tkinter import *
from keyboard import *
from customtkinter import *
import google.generativeai as genai
from tkinter import messagebox



set_appearance_mode("dark")
Font_tuple = ("Comic Sans MS", 15, "bold") 
root = CTk()
root.title("Gemini AI Chat Bot.")
root.geometry("500x600")

def quiz(question):
    genai.configure(api_key="AIzaSyC5pBKVuzGXM2DhWHQXH_aWjkgdqGHxm3o")  # Replace with your actual API key

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

def send():
    if is_pressed('enter'):
        ans()

def ans():
    if userinput.get() == "":
        messagebox.showerror('Error', 'Enter Something To Ask.')

    else:
        try:
            userbutton.configure(state=DISABLED, text="Generating...")
            root.update_idletasks()
            question = "\nYou: " + userinput.get()
            print(question)
            answer = quiz(question)
            answer_text.configure(state=NORMAL)
            answer_text.insert(INSERT, question + "\n")
            answer_text.insert(INSERT, answer + "\n")
            answer_text.configure(state=DISABLED)

        except Exception as e:
            messagebox.showwarning('Error', 'Something Went Wrong!')
            print(e)
        finally:
            # Enable the button and restore its original text
            userbutton.configure(state=NORMAL, text="Send")
def on_enter(event):
    ans()

answer_text = CTkTextbox(root, width=600, height=500, state=DISABLED)
answer_text.place(x=0, y=0) 

answer_text = CTkTextbox(root, width=600, height=500, state=DISABLED)  # Set initial state to disabled
answer_text.place(x=0, y=0)

# TextArea To Type Question
userinput_text = CTkLabel(root, text="Type Here To Search")
userinput_text.place(x=10, y=500)
userinput = CTkEntry(root, placeholder_text="type here to ask....", width=360, height=50)
userinput.place(x=10, y=530)
userbutton = CTkButton(root, text="Send", width=100, height=50, font=Font_tuple, command=ans)
userbutton.place(x=380, y=530)

userinput.bind("<Return>", on_enter)

root.mainloop()

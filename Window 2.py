from tkinter import *
import tkinter as tk
from tkinter import ttk
import TextToSpeech
import pygame

tts = TextToSpeech.Text_to_Speech()
tts.convert_text_to_speech()
name = tts.nameSelf
height = 540
width = 960
root = Tk("Name Game")
root.geometry(str(width) + 'x' + str(height))
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text=name, font = ('Arial', 40)).grid(column=int(width/2), row=5)

sprite = PhotoImage(file = "sprite.png")
sprite2 = PhotoImage(file = 'sprite_GOOD.png')
sprite3 = PhotoImage(file = "sprite_BAD.png")
sprites = [sprite, sprite2, sprite3]
label = sprites[0]
emotion = 0
button = ttk.Button(frm, image = sprites[0])
button.grid(column=int(width/2), row=int(height/2))

def play_audio(recorder):
    pygame.mixer.init()
    pygame.mixer.music.load("test.mp3")
    pygame.mixer.music.play()


def get_text_input():
    entered_text = entry.get()  # Get the text from the Entry widget
    if entered_text == name:
        print("Correct!")  
        sprite_label.config(image=sprite2)
    else:
        print("Try Again!") 
        sprite_label.config(image=sprite3)
root = tk.Tk()
root.title("Text Field Example")

# Create an Entry widget (single-line text field)
entry = tk.Entry(root, width=40)
entry.pack(pady=10)
# Create a Button to submit the text
submit_button = tk.Button(root, text="Submit", command=get_text_input)
submit_button.pack(pady=10)     
# Create a Label to display instructions or feedback
label = tk.Label(root, text="Enter your text above and press Submit")
label.pack(pady=10)


record = ttk.Button(frm, text= 'record', command= lambda: play_audio(tts)).grid(column= 0, row = 0)

root.mainloop()


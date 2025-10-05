from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style
import TextToSpeech
import pygame
from threading import Timer

score = 0
tts = TextToSpeech.TexttoSpeech()
name = tts.name.lower()
tts.convert_text_to_speech()
height = 540
width = 960
root = Tk("Name Game")
root.geometry(str(width) + 'x' + str(height))
frm = ttk.Frame(root, padding=10)
frm.grid()
label = ttk.Label(frm, text=name, font = ('Arial', 40))
#label.grid(column=int(width/2), row=5)

score_label = ttk.Label(frm, text=f"Score: {score}", font=('Arial', 20))
score_label.grid(column=1, row=1)

sprite = PhotoImage(file = "sprite.png")
sprite2 = PhotoImage(file = 'sprite_GOOD.png')
sprite3 = PhotoImage(file = "sprite_BAD.png")
sprites = [sprite, sprite2, sprite3]
emotion = 0
button = ttk.Button(frm, image = sprites[0])
button.grid(column=int(width/2), row=int(height/2))

def play_audio(recorder):
    pygame.mixer.init()
    pygame.mixer.music.load("test.mp3")
    pygame.mixer.music.play()

def get_text_input():
   
    entered_text = entry.get()  # Get the text from the Entry widget
    print(entered_text)
    global name
    global score
    bool = tts.is_correct(entered_text)
    if bool:
        print("Correct!")  
        button.config(image=sprite2)
        button.photo = sprite2
        score += 1
        score_label.configure(text=f"Score: {score}")
        tts.newPerson()
        name = tts.name
        pygame.mixer.music.unload()
        tts.convert_text_to_speech()
        label.configure(text = tts.name)
    else:
        print("Try Again!") 
        button.config(image=sprite3)
        button.photo = sprite3
        score -= 1
        score_label.configure(text=f"Score: {score}")
        entry.delete(0, tk.END)  # Clear the Entry widget
    
  #  t.start()
root = tk.Tk()
root.title("Text Field Example")

# Create an Entry widget (single-line text field)
entry = tk.Entry(root, width=40)
entry.pack(pady=10)
# Create a Button to submit the text
submit_button = tk.Button(root, text="Submit", command=get_text_input)
submit_button.pack(pady=10)     
# Create a Label to display instructions or feedback
elabel = tk.Label(root, text="Enter your text above and press Submit")
elabel.pack(pady=10)

if score >= 10:
        popup = Toplevel(root)
        popup.title("🎉 You Win! 🎉")
        popup.geometry("400x200")
        msg = Label(popup, text="Congratulations! You reached 10 points!", font=('Arial', 16))
        msg.pack(pady=40)
        ok_btn = Button(popup, text="OK", command=root.destroy)  # closes main game
        ok_btn.pack(pady=10)
button.configure(command= lambda: play_audio(tts))
# record = ttk.Button(frm, text= 'speak', command= lambda: play_audio(tts)).grid(column= 0, row = 0)

root.mainloop()

from tkinter import *
from tkinter import ttk
import SpeechToText
import TextToSpeech

name = 'devin'
height = 540
width = 960
root = Tk("Hello World")
root.geometry(str(width) + 'x' + str(height))
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text=name).grid(column=int(width/2), row=5)

sprite = PhotoImage(file = "sprite.png")
sprite2 = PhotoImage(file = 'sprite_GOOD.png')
sprite3 = PhotoImage(file = "sprite_BAD.png")
sprites = [sprite, sprite2, sprite3]
label = sprites[0]
emotion = 0
button = ttk.Button(frm, image = sprites[0])
button.grid(column=int(width/2), row=int(height/2))

def record(but):
    global emotion
    emotion = (emotion + 1) % 3
    but.configure(image = sprites[emotion])
    but.photo = sprites[emotion]
    print(emotion)



record = ttk.Button(frm, text= 'record', command= lambda: record(button)).grid(column= 0, row = 0)

root.mainloop()



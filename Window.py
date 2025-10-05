from tkinter import *
from tkinter import ttk
import SpeechToText

stt = SpeechToText.SpeechToText()
name = stt.nameSelf
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

def name(recorder):
    recorder.record_audio()
    work = recorder.convert_speech_to_text()
    print(work)

record = ttk.Button(frm, text= 'record', command= lambda: name(stt)).grid(column= 0, row = 0)

root.mainloop()



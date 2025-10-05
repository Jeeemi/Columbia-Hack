from tkinter import *
from tkinter import ttk
import SpeechToText

stt = SpeechToText.SpeechToText()
score = 0
lives = 3
name = stt.person.nameSelf
height = 540
width = 960
root = Tk("Name Game")
root.geometry(str(width) + 'x' + str(height))
frm = ttk.Frame(root, padding=10)
frm.grid()
vlabel = ttk.Label(frm, text=name, font = ('Arial', 40))
vlabel.grid(column=int(width/2), row=5)

sprite = PhotoImage(file = "sprite.png")
sprite2 = PhotoImage(file = 'sprite_GOOD.png')
sprite3 = PhotoImage(file = "sprite_BAD.png")
sprites = [sprite, sprite2, sprite3]
label = sprites[0]
emotion = 0
button = ttk.Button(frm, image = sprites[0])
button.grid(column=int(width/2), row=int(height/2))

def name(recorder, but, label):
    recorder.record_audio()
    work = recorder.convert_speech_to_text()
    work = work[:work.__len__() - 1]
    right = recorder.correctPronounciation(work)
    # print('Lives ' + str(lives))
    if right:
        but.configure(image = sprite2)
        but.photo = sprite2
    else:
        print(right)
        but.configure(image = sprite3)
        but.photo = sprite3
    stt.newPerson()
    label.configure(text = stt.name)
        # if lives >= 0:
        #     lives -= 1
        #     name(recorder, but)
        # else:
        #     stt = SpeechToText.SpeechToText()
        #     score -= 1
        #     lives = 3
    print(work)
    print(right)

record = ttk.Button(frm, text= 'record', command= lambda: name(stt, button, vlabel)).grid(column= 0, row = 0)

root.mainloop()



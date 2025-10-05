from tkinter import *
from tkinter import ttk
import SpeechToText
import time
from threading import Timer

stt = SpeechToText.SpeechToText()
score = 0
lives = 3
name = stt.name
height = 540
width = 960
root = Tk("Name Game")
root.geometry(str(width) + 'x' + str(height))
frm = ttk.Frame(root, padding=10)
frm.grid()
vlabel = ttk.Label(frm, text=name, font = ('Arial', 40))
vlabel.grid(column=int(width/2), row=5)

score_label = ttk.Label(frm, text=f"Score: {score}", font=('Arial', 20))
score_label.grid(column=1, row=1)

sprite = PhotoImage(file = "sprite.png")
sprite2 = PhotoImage(file = 'sprite_GOOD.png')
sprite3 = PhotoImage(file = "sprite_BAD.png")
sprites = [sprite, sprite2, sprite3]
emotion = 0
img = ttk.Label(frm, image = sprites[0])
img.grid(column=int(width/2), row=int(height/2))

def revert():
    img.configure(image = sprite)
    img.photo = sprite

def name(recorder, but, label):
    global score
    t = Timer(2, revert)
    recorder.record_audio()
    work = recorder.convert_speech_to_text()
    work = work[:work.__len__() - 1]
    right = recorder.correctPronounciation(work)
    # print('Lives ' + str(lives))
    if right:
        but.configure(image = sprite2)
        but.photo = sprite2
        score += 1
        score_label.configure(text=f"Score: {score}")
    else:
        but.configure(image = sprite3)
        but.photo = sprite3
    print(str(work)+'whaat')
    print(right)
    stt.newPerson()
    print("TEST" + str(stt.name))
    label.configure(text = stt.name)

    if score >= 10:
        popup = Toplevel(root)
        popup.title("🎉 You Win! 🎉")
        popup.geometry("400x200")
        msg = Label(popup, text="Congratulations! You reached 10 points!", font=('Arial', 16))
        msg.pack(pady=40)
        ok_btn = Button(popup, text="OK", command=root.destroy)  # closes main game
        ok_btn.pack(pady=10)
    
        # if lives >= 0:
        #     lives -= 1
        #     name(recorder, but)
        # else:
        #     stt = SpeechToText.SpeechToText()
        #     score -= 1
        #     lives = 3
    t.start()
    

record = ttk.Button(frm, text= 'record', command= lambda: name(stt, img, vlabel)).grid(column= 0, row = 0)

root.mainloop()



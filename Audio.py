from elevenlabs.client import ElevenLabs
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
from elevenlabs import save
import csv
import random
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import SpeechToText
import Text_to_Speech
import Person

class LearnToSpeak:
    Person_ = Person.Person()
    Speech_To_Text = SpeechToText.SpeechToText(Person_)
    Speech_To_Text.correctPronounciation(Speech_To_Text.convert_speech_to_text("audio.wav"))

    
    
































#from pydub import AudioSegment
#from pydub.playback import play

#sets ElevenLabs API
"""
client = ElevenLabs(
    base_url="https://api.elevenlabs.io",
    api_key = 'sk_d1d594a1e078c3f72ac113c704d9b04ecad9906dddb376e1'
)

#records audio
clicked = False
fs = 44100  # Sample rate
seconds = 1  # Duration of recording

with open("audio.wav", "rb") as audio_file: 
    transcript = client.speech_to_text.convert(
        file = audio_file,
        language_code = "eng",
        model_id = "scribe_v1"   # Model for transcription
    )
print(transcript.text)
"""
"""
#rng name
with open('Both Names - Sheet1.csv', 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    # Read all rows into a list
    rows = list(csv_reader)
    # Select a random row from the list
    random_row = random.choice(rows)
    random_name = ','.join(random_row)
    print(random_name)
    person = Person.Person()  # Creates a person with random name from CSV
    print(person.nameSelf)
"""
'''
#text to speech
client = ElevenLabs(
    base_url="https://api.elevenlabs.io",
    api_key = 'sk_d1d594a1e078c3f72ac113c704d9b04ecad9906dddb376e1'
)

audio = client.text_to_speech.convert(
    voice_id="2a4oCZz8wQgpjUB68yHr",
    output_format="mp3_22050_32",
    text= random_name,
    model_id="eleven_multilingual_v2"
)
save(audio, 'test.mp3')

if clicked:
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('audio.wav', fs, myrecording) #saves as file
<<<<<<< Updated upstream
<<<<<<< Updated upstream

def isGood():
    if transcript.text == random_name:
        return True
    else:
        return False
=======
=======
>>>>>>> Stashed changes
'''
'''
root = tk.Tk()
root.title("My Tkinter Window")
root.geometry("960x540")
label = tk.Label(root, text="Press the button below")
label.pack(pady=20)

def on_button_click():
    label.config(text="🎤 Button clicked!")

img = Image.open("Neutral.png")
img = img.resize((250, 250))  # Resize to fit nicely
photo = ImageTk.PhotoImage(img)

button = tk.Button(
    root,
    text= photo,
    command=on_button_click,  # Run this when pressed
    borderwidth=0,            # No frame around the image
    bg="#222",                # Match background color
    activebackground="#222"   # Prevent white flash on click
)
button.pack(pady=10)
root.mainloop()
<<<<<<< Updated upstream
'''
>>>>>>> Stashed changes
=======
'''
>>>>>>> Stashed changes

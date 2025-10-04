from elevenlabs.client import ElevenLabs
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
from elevenlabs import save
import csv
import random

#from pydub import AudioSegment
#from pydub.playback import play

#sets ElevenLabs API
client = ElevenLabs(
    base_url="https://api.elevenlabs.io",
    api_key = 'sk_d1d594a1e078c3f72ac113c704d9b04ecad9906dddb376e1'
)

#records audio
fs = 44100  # Sample rate
seconds = 1  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('audio.wav', fs, myrecording) #saves as file

with open("audio.wav", "rb") as audio_file: 
    transcript = client.speech_to_text.convert(
        file = audio_file,
        language_code = "eng",
        model_id = "scribe_v1"   # Model for transcription
    )
print(transcript.text)
#rng name
with open('Both Names - Sheet1.csv', 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    # Read all rows into a list
    rows = list(csv_reader)
    # Select a random row from the list
    random_row = random.choice(rows)
    random_name = ','.join(random_row)
    print(random_name)
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

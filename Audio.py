from elevenlabs.client import ElevenLabs
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

#sets ElevenLabs API
client = ElevenLabs(
    base_url="https://api.elevenlabs.io",
    api_key = userdata.get('secretName')
)

#records audio
fs = 44100  # Sample rate
seconds = 4  # Duration of recording

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

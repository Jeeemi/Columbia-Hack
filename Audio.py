from elevenlabs.client import ElevenLabs
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
from elevenlabs import save
from pydub import AudioSegment
from pydub.playback import play

#sets ElevenLabs API
client = ElevenLabs(
    base_url="https://api.elevenlabs.io",
    api_key = userdata.get('secretstuff')
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

#text to speech
client = ElevenLabs(
    base_url="https://api.elevenlabs.io",
    api_key = 'sk_d1d594a1e078c3f72ac113c704d9b04ecad9906dddb376e1'
)

audio = client.text_to_speech.convert(
    voice_id="xctasy8XvGp2cVO9HL9k",
    output_format="mp3_22050_32",
    text="THIS IS A TEST",
    model_id="eleven_multilingual_v2"
)

save(audio, 'test.mp3')

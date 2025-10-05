
from elevenlabs.client import ElevenLabs
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
from elevenlabs import save
import Person

class SpeechToText:
    def __init__(self):
        self.client = ElevenLabs(
            base_url="https://api.elevenlabs.io",
            api_key = 'sk_d1d594a1e078c3f72ac113c704d9b04ecad9906dddb376e1'
        )
    
    def record_audio(self,
            fs = 44100,  # Sample rate
            seconds = 1  # Duration of recording
        ):
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()  # Wait until recording is finished
        write('audio.wav', fs, myrecording) #saves as file
            

    def convert_speech_to_text(self, audio_file_path='audio.wav'):
        with open(audio_file_path, "rb") as audio_file:
            transcript = self.client.speech_to_text.convert(
                file=audio_file,
                language_code="eng",
                model_id="scribe_v1"   # Model for transcription
            )
        spoken_text = transcript.text
        return spoken_text

    def correctPronounciation(self, spoken_text, rightName):
        while ((spoken_text == rightName) == False):
            spoken_text = self.convert_speech_to_text("audio.wav")
        return True

'''
        # Example usage
        stt = SpeechToText()
        transcript_text = stt.convert_speech_to_text("audio.wav")
        print(transcript_text)
'''

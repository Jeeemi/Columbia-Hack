from elevenlabs.client import ElevenLabs
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
from elevenlabs import save
import Person
class Text_to_Speech:
    
    client = ElevenLabs(
        base_url="https://api.elevenlabs.io",
        api_key = 'sk_d1d594a1e078c3f72ac113c704d9b04ecad9906dddb376e1'
    )
    person = Person.Person()
    nameSelf = person.nameSelf
    print(nameSelf)

    def convert_text_to_speech(self,  text=nameSelf, voice_id="2a4oCZz8wQgpjUB68yHr", output_format="mp3_22050_32", model_id="eleven_multilingual_v2", filename='test.mp3'):
        audio = self.client.text_to_speech.convert(
            text=text,
            voice_id=voice_id,
            output_format=output_format,
            model_id=model_id
        )
        save(audio, filename)


# Example usage:
# tts = Text_to_Speech()
# tts.convert_text_to_speech(Person.Person().nameSelf)

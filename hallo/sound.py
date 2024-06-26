import wave
import sys

import pyaudio

CHUNK = 1024


def sound(path, file_name):
    file_with_extension = path + '/' + file_name + '.wav'
    with wave.open(file_with_extension, 'rb') as wf:
        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        while len(data := wf.readframes(CHUNK)):
            stream.write(data)

        stream.close()

        p.terminate()




#!/usr/bin/python3

import pyaudio
import sys
import wave
from pydub import AudioSegment

filename = 'piano2.wav'
chunk = 1024

pd = AudioSegment.from_file(filename)

p = pyaudio.PyAudio()

stream = p.open(format = p.get_format_from_width(pd.sample_width),
                channels = pd.channels,
                rate = pd.frame_rate,
                output = True)

i = 0
data = pd[:chunk]._data

while data:
    stream.write(data)
    i += chunk
    data = pd[i:i+chunk]._data

stream.close()
p.terminate()
sys.exit(0)

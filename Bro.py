#got this code from pyaudio 
#first install pyaduio and wave and sys
#os should already be in your python file you installed
import pyaudio
import wave
import sys

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1 if sys.platform == 'darwin' else 2
RATE = 44100
RECORD_SECONDS = 5
OUTPUT_FILENAME = '/usr/lib/Pyaudio/desktop_audio.wav'

p = pyaudio.PyAudio()

device_index = 2

print(f"Recording from: {p.get_device_info_by_index(device_index)['name']}")

stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK, input_device_index=device_index)

print('Recording...')
frames = []

for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
      data = stream.read(CHUNK)
      frames.append(data)
print('Done')

stream.stop_stream()
stream.close()

import os 
os.makedirs("/usr/lib/Pyaudio/desktop_audio.wav", exist_ok=True)
wf = wave.open(OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

print(f"Saved to {OUTPUT_FILENAME}")

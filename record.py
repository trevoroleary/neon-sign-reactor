import soundcard as sc
import pyaudio
import time
import numpy as np
from matplotlib import pyplot as plt
import wave


speakers = sc.all_speakers()
print(speakers)
mics = sc.all_microphones()
print(mics)

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = 'filename'

p = pyaudio.PyAudio()
fulldata = np.array([])
dry_data = np.array([])


def main():
    stream = p.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK,
                    input_device_index=2)

    print("recording...")
    print('---------------------------------')
    print(int(RATE / CHUNK * RECORD_SECONDS))
    print('*********************************')

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        print("Recording . . .")

        frames.append(data)
    print("Recording finished. . .")

    # stop Recording
    stream.stop_stream()
    stream.close()
    p.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(2)
    audio.get_sample_size(FORMAT)
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()


def callback(in_data, frame_count, time_info, flag):
    global b,a,fulldata,dry_data,frames
    audio_data = np.fromstring(in_data, dtype=np.float32)
    dry_data = np.append(dry_data,audio_data)
    #do processing here
    fulldata = np.append(fulldata,audio_data)
    return (audio_data, pyaudio.paContinue)


main()
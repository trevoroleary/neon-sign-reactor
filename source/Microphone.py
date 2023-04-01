import logging
import pyaudio
import numpy as np
import logging

class Microphone:
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000 # The other mic works at 44100
    CHUNK = 1024 # RATE / number of updates per second
    window = np.blackman(CHUNK) # Decaying window on either side of chunk

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.audio_driver = pyaudio.PyAudio()
        self.input_stream = self.audio_driver.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.RATE,
            input=True, 
            frames_per_buffer=self.CHUNK, 
            input_device_index=2)
        
    def listen(self):
        return self.input_stream.read(self.CHUNK, exception_on_overflow=False)

class RazerMicrophone(Microphone):
    RATE = 16000
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(__name__)

class AmazonMicrophone(Microphone):
    RATE = 44100
    def __init__(self):
        super().__init__()
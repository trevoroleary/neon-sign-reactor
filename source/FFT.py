import logging
import wave
import numpy as np

class FFT:
    # FFT Moving Average Settings
    WINDOW_SIZE = 4
    LEVELS = [0]*WINDOW_SIZE # Window of brightness levels for neon

    def __init__(self, chunk: int):
        self.chunk = chunk
        self.logger = logging.getLogger(__name__)
        self.window = np.blackman(chunk) # Decaying window on either side of chunk

    def get_frequency_data(self, audio_data):
        waveData = wave.struct.unpack("%dh"%(self.chunk), audio_data)
        npArrayData = np.array(waveData)
        indata = npArrayData*self.window
        fft_data = np.abs(np.fft.rfft(indata))
        return fft_data
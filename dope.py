import pyaudio
import numpy as np
import time
import wave
# import matplotlib.pyplot as plt
from gpiozero import LED, PWMLED
from time import sleep
import _thread

LED_PINS = [18, 12, 19]
leds = [PWMLED(pin, frequency=100, active_high=False) for pin in LED_PINS]

def pulse():
    for i in range(100, 0, -1):
        for led in leds:
            led.value = i/100
        sleep(0.001)
    led.off()

# open stream
FORMAT = pyaudio.paInt16
CHANNELS = 1
# RATE = 44100
RATE = 16000
# RATE = 8000

CHUNK = 1024 # RATE / number of updates per second

RECORD_SECONDS = 1000


# use a Blackman window
window = np.blackman(CHUNK)

x = 0


def soundPlot(stream):
    t1 = time.time()
    data = stream.read(CHUNK, exception_on_overflow=False)
    waveData = wave.struct.unpack("%dh"%(CHUNK), data)
    npArrayData = np.array(waveData)
    indata = npArrayData*window

    fftData=np.abs(np.fft.rfft(indata))
    # fftTime=np.fft.rfftfreq(CHUNK, 1./RATE)
    which = fftData[1:].argmax() + 1

    # use quadratic interpolation around the max
    if which != len(fftData)-1:
        y0,y1,y2 = np.log(fftData[which-1:which+2:])
        x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
        # find the frequency and output it
        thefreq = (which+x1)*RATE/CHUNK
        # print("The freq is %f Hz." % (thefreq))
    else:
        thefreq = which*RATE/CHUNK
        # print("The freq is %f Hz." % (thefreq))

    thresh = 100000
    freq_range = fftData[1:5]
    if any(y > thresh for y in freq_range):
        _thread.start_new_thread(pulse, ())


if __name__=="__main__":
    p=pyaudio.PyAudio()
    stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
                  frames_per_buffer=CHUNK, input_device_index=2)

    # plt.ion()
    # fig = plt.figure(figsize=(10, 8))
    # ax1 = fig.add_subplot(211)
    # ax2 = fig.add_subplot(212)

    # for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    while True:
        soundPlot(stream)

    stream.stop_stream()
    stream.close()
    p.terminate()

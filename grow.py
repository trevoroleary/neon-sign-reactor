import pyaudio
import numpy as np
import time
import wave
# import matplotlib.pyplot as plt
from gpiozero import LED, PWMLED
from time import sleep
import _thread
from random import random

LED_PINS = [18, 12, 19]
leds = [PWMLED(pin, frequency=100, active_high=False) for pin in LED_PINS]

def up_down(led):
    for i in range(100, 0, -1):
        leds[led].value = i/100
        sleep(0.05)
    for i in range(101):
        leds[led].value = i/100
        sleep(0.05)

while True:
    sleep(random()*3)
    up_down(int(random()*3)


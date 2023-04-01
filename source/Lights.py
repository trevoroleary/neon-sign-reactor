from gpiozero import LED, PWMLED
from time import sleep
import logging
import _thread

LED_PINS = [18, 12, 19]


class NeonLight:
    HIGH_THRESH = 0.3e6 # The high threshold of frequency power. If a frequency is beyond this lights often pulse or go 100%
    LOW_THRESH = 0.05e6 # Any sound below the low threshold will not triggery any light behavior
    REST_LEVEL = 0.02 # what duty cycle (on level) will the lights be at rest
    WINDOW_SIZE = 4 # How many samples in the moving window

    RED_LEDS = [1,2]

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.level = 0
        self.moving_window_levels = [0]*self.WINDOW_SIZE
        self.leds = [PWMLED(pin, frequency=100, active_high=False) for pin in LED_PINS]

    def set_level(self):
        level = sum(self.moving_window_levels)
        if level > 1:
            level = 1
        for i, led in enumerate(self.leds):
            attenuate = 2 if i in self.RED_LEDS else 1
            led.value = level/attenuate

    def pulse(self):
        for i in range(100, 0, -1):
            for i, led in enumerate(self.leds):
                attenuate = 2 if i in self.RED_LEDS else 1
                led.value = i/attenuate/100
            sleep(0.005)
        led.off()
    
    def loud_reaction(self, highest_frequency_power, offset):
        self.moving_window_levels = [
            (highest_frequency_power - self.LOW_THRESH) / (self.WINDOW_SIZE*(self.HIGH_THRESH - self.LOW_THRESH)) + offset
            ]*self.WINDOW_SIZE
        _thread.start_new_thread(self.pulse, ())

    def volume_reaction(self, highest_frequency_power, offset):
        self.moving_window_levels.append(
            (highest_frequency_power - self.LOW_THRESH)/(self.WINDOW_SIZE*(self.HIGH_THRESH - self.LOW_THRESH)) + offset)
        self.moving_window_levels.pop(0)
        _thread.start_new_thread(self.set_level, ())
    
    def quiet_reaction(self):
        self.moving_window_levels.append(0)
        self.moving_window_levels.pop(0)
        _thread.start_new_thread(self.set_level, ())




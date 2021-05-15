import threading, queue

import RPi.GPIO as GPIO
from gpiozero import LED, PWMLED
from time import sleep


LED_PINS = [18, 12, 19]
LED_PIN = 18

def cycle():
    red = LED(18)
    yellow = LED(12)
    green = LED(19)
    sleep_time = 0.1
    while True:
        red.on()
        sleep(sleep_time)
        yellow.on()
        sleep(sleep_time)
        green.on()
        sleep(sleep_time)
        red.off()
        sleep(sleep_time)
        yellow.off()
        sleep(sleep_time)
        green.off()
        sleep(sleep_time)

def test():
    leds = [PWMLED(pin, frequency=1000) for pin in LED_PINS]

    while True:
        for led in leds:
            for i in range(100, 0, -1):
                led.value = i/100
                sleep(0.01)
            led.off()


def pulse():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED_PIN, GPIO.OUT)
    pi_pwm = GPIO.PWM(LED_PIN, 1000)
    pi_pwm.start(0)



# pulse()
# test()
# cycle()
import threading
import time

from RPi import GPIO

from Toggleable import Toggleable

click_time = 0.06


class OutletSwitch(Toggleable):
    def __init__(self, on_pin, off_pin):
        super().__init__()
        self.on_pin = on_pin
        self.off_pin = off_pin
        GPIO.setup(on_pin, GPIO.OUT)
        GPIO.setup(off_pin, GPIO.OUT)
        GPIO.output(self.on_pin, GPIO.HIGH)
        GPIO.output(self.off_pin, GPIO.HIGH)

    def _execute_set_on(self):
        GPIO.output(self.on_pin, GPIO.LOW)
        time.sleep(click_time)
        GPIO.output(self.on_pin, GPIO.HIGH)

    def _execute_set_off(self):
        GPIO.output(self.off_pin, GPIO.LOW)
        time.sleep(click_time)
        GPIO.output(self.off_pin, GPIO.HIGH)

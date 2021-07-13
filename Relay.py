import time
from RPi import GPIO

from Toggleable import Toggleable


class Relay(Toggleable):
    def __init__(self, pin):
        super().__init__()

        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def _execute_set_on(self):
        GPIO.output(self.pin, GPIO.HIGH)
        super()._execute_set_on()

    def _execute_set_off(self):
        GPIO.output(self.pin, GPIO.LOW)
        super()._execute_set_off()

    def pulse(self):
        try:
            self.set_on()
            time.sleep(0.1)
        finally:
            self.set_off()
        self.set_off()

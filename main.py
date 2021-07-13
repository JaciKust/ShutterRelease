import time

from RPi import GPIO

from Button import Button
from Relay import Relay


class Runner:
    def __init__(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        self.focus_relay = Relay(5)
        self.shoot_relay = Relay(6)

        self.top_button = Button(23)
        self.middle_button = Button(24)
        self.bottom_button = Button(25)

        self.bottom_button.button_events.on_depressed += self.shoot

    def shoot(self, trigger_pin):
        self.take_photo(1)

    def take_photo(self, time_in_seconds):
        self.focus_relay.set_on()
        time.sleep(0.1)

        self.shoot_relay.set_on()
        time.sleep(time_in_seconds)

        self.shoot_relay.set_off()
        self.focus_relay.set_off()


if __name__ == '__main__':
    Runner()

    while True:
        time.sleep(1)


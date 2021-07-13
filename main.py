import time

from RPi import GPIO

from Button import Button
from Relay import Relay
from RgbLed import RgbLed
import Color as ColorConstant
from Wand import Wand


class Runner:
    def __init__(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        self.focus_relay = Relay(5)
        self.shoot_relay = Relay(6)

        self.wand = Wand(18, 27, 22, 23, 24, 25)

        self.wand.bottom_button.button_events.on_depressed += self.shoot

    def shoot(self, trigger_pin):
        self.take_photo(1)

    def take_photo(self, time_in_seconds):
        self.wand.led.set_color(ColorConstant.DIM_RED)
        self.focus_relay.set_on()
        time.sleep(0.1)
        self.wand.led.set_color(ColorConstant.DIM_GREEN)
        self.shoot_relay.set_on()
        time.sleep(time_in_seconds)

        self.shoot_relay.set_off()
        self.focus_relay.set_off()
        self.wand.led.set_color(ColorConstant.DIM_BLUE)


if __name__ == '__main__':
    Runner()

    while True:
        time.sleep(1)


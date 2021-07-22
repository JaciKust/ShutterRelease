import time
from RPi import GPIO
import Color as ColorConstant
from Wand import Wand


class Runner:
    def __init__(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        self.blue_wand = Wand(19, 16, 13, 12, 6, 5)
        self.red_wand = Wand(4, 17, 18, 27, 20, 21)

        self.blue_wand.white_button.button_events.on_depressed += self.flash_red
        self.blue_wand.yellow_button.button_events.on_depressed += self.flash_green
        self.blue_wand.black_button.button_events.on_depressed += self.flash_blue

        self.red_wand.white_button.button_events.on_depressed += self.flash_red
        self.red_wand.yellow_button.button_events.on_depressed += self.flash_green
        self.red_wand.black_button.button_events.on_depressed += self.flash_blue

        self.blue_wand.led.set_color(ColorConstant.BLACK)

    def flash_red(self, trigger_pin=None):
        self.flash_color(ColorConstant.DIM_RED)

    def flash_green(self, trigger_pin=None):
        self.flash_color(ColorConstant.DIM_GREEN)

    def flash_blue(self,  trigger_pin=None):
        self.flash_color(ColorConstant.DIM_BLUE)

    def flash_color(self, color):
        self.red_wand.led.set_color(color)
        self.blue_wand.led.set_color(color)
        time.sleep(1)
        self.red_wand.led.set_color(ColorConstant.BLACK)
        self.blue_wand.led.set_color(ColorConstant.BLACK)


if __name__ == '__main__':
    Runner()

    while True:
        time.sleep(1)


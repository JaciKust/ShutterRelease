import time
from RPi import GPIO
import Color as ColorConstant
from RgbLed import RgbLed
from Wand import Wand


class Runner:
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)

        self.led = RgbLed(16, 20, 21)
        time.sleep(2)
        colors = [
            ColorConstant.RED,
            ColorConstant.GREEN,
            ColorConstant.BLUE,

            ColorConstant.CYAN,
            ColorConstant.MAGENTA,
            ColorConstant.YELLOW,

            ColorConstant.WHITE,

            ColorConstant.DIM_RED,
            ColorConstant.DIM_GREEN,
            ColorConstant.DIM_BLUE,

            ColorConstant.DARK_RED,
            ColorConstant.DARK_GREEN,
            ColorConstant.DARK_BLUE,

            ColorConstant.DIM_MAGENTA,
            ColorConstant.DIM_CYAN,
            ColorConstant.DIM_YELLOW,

            ColorConstant.DARK_MAGENTA,
            ColorConstant.DARK_CYAN,
            ColorConstant.DARK_YELLOW,

            ColorConstant.DIM_WHITE,
            ColorConstant.DARK_WHITE,
            ColorConstant.DIMMEST_WHITE,
        ]

        for c in colors:
            self.flash_color(c)

    def flash_red(self, trigger_pin=None):
        self.flash_color(ColorConstant.DIM_RED)

    def flash_green(self, trigger_pin=None):
        self.flash_color(ColorConstant.DIM_GREEN)

    def flash_blue(self,  trigger_pin=None):
        self.flash_color(ColorConstant.DIM_BLUE)

    def flash_color(self, color):
        self.led.set_color(color)
        time.sleep(0.5)


if __name__ == '__main__':
    Runner()


import time

from RPi import GPIO

from Camera import Camera
from RgbLed import RgbLed
import Color as ColorConstant


class Runner:
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)

        led = RgbLed(19, 16, 13)

        led.set_color(ColorConstant.MAGENTA)
        c = Camera(20, 21)
        c.focus()
        time.sleep(0.5)
        c.take_photo(0.5)
        led.set_color(ColorConstant.BLACK)


if __name__ == '__main__':
    Runner()

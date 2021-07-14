import time
from RPi import GPIO
import Color as ColorConstant
from Camera import Camera
from Wand import Wand


class Runner:
    def __init__(self):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        self.wand = Wand(18, 27, 22, 23, 24, 25)
        self.camera = Camera(5, 6)

        self.wand.white_button.button_events.on_depressed += self.shoot

        self.wand.led.set_color(ColorConstant.GREEN)


    def shoot(self, trigger_pin):
        shoot_time = 1
        self.wand.led.set_color(ColorConstant.BLACK)
        self.camera.take_photo(shoot_time)
        self.wand.led.set_color(ColorConstant.DIM_RED)
        time.sleep(shoot_time)
        self.wand.led.set_color(ColorConstant.DIM_GREEN)


if __name__ == '__main__':
    Runner()

    while True:
        time.sleep(1)


from Button import Button
from RgbLed import RgbLed


class Wand:
    def __init__(self, red_led_pin, green_led_pin, blue_led_pin, top_button_pin, middle_button_pin, bottom_button_pin):
        self.led = RgbLed(red_led_pin, green_led_pin, blue_led_pin)

        self.black_button = Button(top_button_pin)
        self.yellow_button = Button(middle_button_pin)
        self.white_button = Button(bottom_button_pin)

from RPi import GPIO
import Color as ColorConstant


class RgbLed:
    def __init__(self, red_led_pin, green_led_pin, blue_led_pin):
        self.LED_MAXIMUM = 100

        GPIO.setup(red_led_pin, GPIO.OUT)
        GPIO.setup(green_led_pin, GPIO.OUT)
        GPIO.setup(blue_led_pin, GPIO.OUT)
        self.previous_color = None

        self.red_led = GPIO.PWM(red_led_pin, ColorConstant.FULL)
        self.green_led = GPIO.PWM(green_led_pin, ColorConstant.FULL)
        self.blue_led = GPIO.PWM(blue_led_pin, ColorConstant.FULL)

        self.red_led.start(100)
        self.green_led.start(100)
        self.blue_led.start(100)

    def set_color(self, color):
        if self.previous_color == color:
            return
        self.previous_color = color
        self.red_led.ChangeDutyCycle(color.as_rgb_array()[ColorConstant.RED_LOCATION])
        self.green_led.ChangeDutyCycle(color.as_rgb_array()[ColorConstant.GREEN_LOCATION])
        self.blue_led.ChangeDutyCycle(color.as_rgb_array()[ColorConstant.BLUE_LOCATION])

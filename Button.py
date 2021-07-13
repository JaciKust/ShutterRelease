import sys
import time
from datetime import datetime

from RPi import GPIO
from Constants import Button as ButtonConstant
import cEvent


class Button:
    current_color = None
    previous_color = None
    LED_MAXIMUM = 100

    def __init__(self, trigger_pin):
        GPIO.setup(trigger_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(
            trigger_pin,
            GPIO.RISING,
            callback=self._capture_button_press,
            bouncetime=ButtonConstant.BOUNCE_TIME_MS
        )

        self.trigger_pin = trigger_pin
        self.button_events = cEvent.Events()

    _is_pressed = False

    # 'channel' is unused because we know the trigger pin already.
    def _capture_button_press(self, channel):
        try:
            if self._is_pressed:
                return

            self._is_pressed = True
            button_start_press_time = time.time()
            time.sleep(0.01)

            self.wait_for_button_release()
            button_press_time = time.time() - button_start_press_time

            if button_press_time < ButtonConstant.NOISE_THRESHOLD:
                # Write off as noise -- ignore.
                self._is_pressed = False
                return

            self.log_data("{} Button pressed for {} seconds".format(self.trigger_pin, round(button_press_time, 3)))

            self.button_events.on_depressed(self.trigger_pin)

        except Exception:
            t, v, tb = sys.exc_info()
            self.log_data("An error was encountered of type: {}".format(t))
            self.log_data("Value: {}".format(v))
            self.log_data(str(tb))
            raise
        finally:
            self._is_pressed = False

    def wait_for_button_release(self):
        while GPIO.input(self.trigger_pin) == ButtonConstant.BUTTON_PRESSED_VALUE:
            time.sleep(0.01)

    def log_data(self, data):
        now = str(datetime.now())
        data = str(data)
        output = '[{}] {}'.format(now, data)
        print(output)

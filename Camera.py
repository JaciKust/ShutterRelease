import time
from Relay import Relay


class Camera:
    def __init__(self, focus_pin, shoot_pin):
        self.focus_relay = Relay(focus_pin)
        self.shoot_relay = Relay(shoot_pin)

    def take_photo(self, time_in_seconds):
        self.focus_relay.set_on()
        time.sleep(0.1)

        self.shoot_relay.set_on()
        time.sleep(time_in_seconds)

        self.shoot_relay.set_off()
        self.focus_relay.set_off()


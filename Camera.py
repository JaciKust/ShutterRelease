import time
from Relay import Relay


class Camera:
    def __init__(self, focus_pin, shoot_pin):
        self.focus_relay = Relay(focus_pin)
        self.shoot_relay = Relay(shoot_pin)

        self.focus_relay.set_off()
        self.shoot_relay.set_off()
        self.is_focused = False

    def take_photo(self, time_in_seconds):

        time.sleep(0.1)

        self.shoot_relay.set_on()
        time.sleep(time_in_seconds)

        self.shoot_relay.set_off()
        self.focus_relay.set_off()

    def focus(self):
        if self.is_focused:
            print('already focused!')
        self.focus_relay.set_on()
        self.is_focused = True

    def defocus(self):
        self.focus_relay.set_off()
        self.is_focused = False

    def refocus(self, sleep_time=0.1):
        self.defocus()
        time.sleep(sleep_time)
        self.focus()

    def shoot(self, shutter_time=None):
        #assert(self.is_focused, "Must be focused inable to take a photo.")
        if not self.is_focused:
            print("Not focused!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        if shutter_time is None:
            # Default to ~1/60th of a second
            shutter_time = 0.016

        self.shoot_relay.set_on()
        print("Sleeping for: " + str(shutter_time))
        time.sleep(shutter_time)
        print("Done shooting, turning off. ")
        self.shoot_relay.set_off()
        self.defocus()



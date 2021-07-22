import time
from RPi import GPIO

from OutletSwitch import OutletSwitch


class Runner:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        switch1 = OutletSwitch(4, 17)
        switch2 = OutletSwitch(18, 27)
        switch3 = OutletSwitch(16, 19)
        switch4 = OutletSwitch(20, 21)

        switch1.set_on()
        switch2.set_on()
        switch4.set_on()
        switch3.set_on()

        time.sleep(0.2)
        switch1.set_off()
        switch2.set_off()
        switch3.set_off()
        switch4.set_off()

    def toggle(self, switch):
        switch.set_on()
        time.sleep(2)
        switch.set_off()
        time.sleep(2)


if __name__ == '__main__':
    Runner()
    GPIO.cleanup()

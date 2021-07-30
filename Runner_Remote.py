"""
Example for using the RFM69HCW Radio with Raspberry Pi.

Learn Guide: https://learn.adafruit.com/lora-and-lorawan-for-raspberry-pi
Author: Brent Rubell for Adafruit Industries
"""
# Import Python System Libraries
import json
import time
# Import Blinka Libraries
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
# Import the SSD1306 module.
import adafruit_ssd1306
# Import the RFM69 radio module.
import adafruit_rfm69

from DataObjects.Focus import FocusDataObject
from DataObjects.LightState import LightState
from DataObjects.Shoot import ShootDataObject
from DataObjects.Reset import ResetDataObject
from Wand import Wand
import Color as ColorConstant


class Runner:
    def __init__(self):
        # Configure Packet Radio
        CS = DigitalInOut(board.CE1)
        RESET = DigitalInOut(board.D25)
        spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
        self.rfm69 = adafruit_rfm69.RFM69(spi, CS, RESET, 915.0)
        prev_packet = None

        # Optionally set an encryption key (16 byte AES key). MUST match both
        # on the transmitter and receiver (or be set to None to disable/the default).
        self.rfm69.encryption_key = b'\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x07\x08'

        self.red_wand = Wand(12, 13, 16, 19, 20, 21)
        self.red_wand.yellow_button.button_events.on_depressed += self.shoot
        self.red_wand.black_button.button_events.on_depressed += self.focus
        self.red_wand.white_button.button_events.on_depressed += self.reset

        self.red_wand.led.set_color(ColorConstant.RED)

    def send(self, data):
        data = json.dumps(data.__dict__)
        data = bytes(data + "\r\n","utf-8")
        self.rfm69.send(data)

    def simple_shoot(self, channel=None):
        # What I used testing in Denver.
        self.send(LightState(1, 'on'))
        time.sleep(0.1)
        self.send(ShootDataObject())
        self.red_wand.led.set_color(ColorConstant.BLUE)
        time.sleep(0.5)
        self.send(LightState(1, 'off'))
        time.sleep(0.4)
        self.red_wand.led.set_color(ColorConstant.RED)

    def toggle_all(self, channel=None):
        t = 0.1
        self.send(LightState(1, 'on'))
        time.sleep(t)
        self.send(LightState(2, 'on'))
        time.sleep(t)
        self.send(LightState(3, 'on'))
        time.sleep(t)
        self.send(LightState(4, 'on'))

        time.sleep(0.5)

        self.send(LightState(1, 'off'))
        time.sleep(t)
        self.send(LightState(2, 'off'))
        time.sleep(t)
        self.send(LightState(3, 'off'))
        time.sleep(t)
        self.send(LightState(4, 'off'))

    def shoot(self, channel=None):
        self.toggle_all()

    def focus(self, channel=None):
        self.send(FocusDataObject())
        self.red_wand.led.set_color(ColorConstant.GREEN)

    def reset(self, channel=None):
        print('resetting')
        self.send(ResetDataObject())


if __name__ == '__main__':
    r = Runner()
    while True:
        time.sleep(0.1)

# 0.1 second delay after changing an outlet state


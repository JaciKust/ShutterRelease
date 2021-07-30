"""
Example for using the RFM69HCW Radio with Raspberry Pi.

Learn Guide: https://learn.adafruit.com/lora-and-lorawan-for-raspberry-pi
Author: Brent Rubell for Adafruit Industries
"""
# Import Python System Libraries
import json
import time
# Import Blinka Libraries
from collections import namedtuple

import busio
from digitalio import DigitalInOut, Direction, Pull
import board
# Import the SSD1306 module.
import adafruit_ssd1306
# Import the RFM69 radio module.
import adafruit_rfm69

from Camera import Camera
from OutletSwitch import OutletSwitch


class Runner:
    def __init__(self):
        self.restart = False

        # Configure Packet Radio
        CS = DigitalInOut(board.CE1)
        RESET = DigitalInOut(board.D25)
        spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
        self.rfm69 = adafruit_rfm69.RFM69(spi, CS, RESET, 915.0)
        prev_packet = None

        # Optionally set an encryption key (16 byte AES key). MUST match both
        # on the transmitter and receiver (or be set to None to disable/the default).
        self.rfm69.encryption_key = b'\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x07\x08'

        self.switch1 = OutletSwitch(4, 17)


    def _decoder(self, dict):
        return namedtuple('X', dict.keys())(*dict.values())

    def check_for_message(self):
        packet = None

        # check for packet rx
        packet = self.rfm69.receive()
        prev_packet = packet
        packet_text = str(prev_packet, "utf-8")
        data = json.loads(packet_text, object_hook=self._decoder)
        print('Name: ' + data.name)

        self.run_logic(data)

    def run_logic(self, command):
        if command.name == 'LightState':
            if command.state == 'on':
                self.switch1.set_on()
            else:
                self.switch1.set_off()
        if command.name == 'Reset':
            self.restart = True


class Manager:
    def __init__(self):
        self.runner = None
        self.init()
        while True:
            try:
                self.loop()
                if self.runner.restart:
                    self.re_init()

            except Exception as e:
                print(e)

    def init(self):
        print('Starting!')
        self.runner = Runner()

    def loop(self):
        self.runner.check_for_message()

    def re_init(self):
        print('Restarting!')
        self.init()


if __name__ == '__main__':
    Manager()
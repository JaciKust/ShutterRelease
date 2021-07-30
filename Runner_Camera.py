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


class Runner:
    def __init__(self):
        # Create the I2C interface.
        self.restart = False
        i2c = busio.I2C(board.SCL, board.SDA)

        # 128x32 OLED Display
        reset_pin = DigitalInOut(board.D4)
        self.display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, reset=reset_pin)
        # Clear the display.
        self.display.fill(0)
        self.display.show()
        self.display_width = self.display.width
        self.display_height = self.display.height

        self.camera = Camera(20, 21)

        # Configure Packet Radio
        CS = DigitalInOut(board.CE1)
        RESET = DigitalInOut(board.D25)
        spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
        self.rfm69 = adafruit_rfm69.RFM69(spi, CS, RESET, 915.0)
        prev_packet = None

        # Optionally set an encryption key (16 byte AES key). MUST match both
        # on the transmitter and receiver (or be set to None to disable/the default).
        self.rfm69.encryption_key = b'\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x07\x08'

    def _decoder(self, dict):
        return namedtuple('X', dict.keys())(*dict.values())

    def check_for_message(self):
        packet = None
        # draw a box to clear the image
        self.display.fill(0)
        self.display.text('RasPi Radio', 35, 0, 1)

        # check for packet rx
        packet = self.rfm69.receive()
        if packet is None:
            self.display.show()
            self.display.text('- Waiting for PKT -', 15, 20, 1)
        else:
            self.display.fill(0)
            prev_packet = packet
            packet_text = str(prev_packet, "utf-8")
            data = json.loads(packet_text, object_hook=self._decoder)
            print('Name: ' + data.name)

            self.run_logic(data)

    def run_logic(self, command):
        if command.name == 'Focus':
            print("Focusing!")
            self.camera.focus()
        elif command.name == 'Shoot':
            print("Shooting!")
            self.camera.shoot()
        # elif command.name == 'Wait':
        #     time.sleep(command.time)
        elif command.name == 'Reset':
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


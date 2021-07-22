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


class Runner:
    def __init__(self):
        # Create the I2C interface.
        i2c = busio.I2C(board.SCL, board.SDA)

        # 128x32 OLED Display
        reset_pin = DigitalInOut(board.D4)
        self.display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, reset=reset_pin)
        # Clear the display.
        self.display.fill(0)
        self.display.show()
        self.display_width = self.display.width
        self.display_height = self.display.height

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
            time.sleep(1)


if __name__ == '__main__':
    r = Runner()

    while True:
        r.check_for_message()

import colorsys


class Color:

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
        self._calc_hsv()

    hue = None
    saturation = None
    value = None

    def _calc_hsv(self):
        r = self.red / 100.0
        g = self.green / 100.0
        b = self.blue / 100.0

        h, s, v = colorsys.rgb_to_hsv(r, g, b)
        multiplier = 65535
        self.hue = h * multiplier
        self.saturation = s * multiplier
        self.value = v * multiplier

    def as_rgb_array(self):
        return [
            self.red,
            self.green,
            self.blue,
        ]

    def as_hsv_array(self):
        return [
            self.hue,
            self.saturation,
            self.value,
        ]

RED_LOCATION = 0
GREEN_LOCATION = 1
BLUE_LOCATION = 2

DIM = 20
DARK = 1
FULL = 100
OFF = 0

RED = Color(FULL, OFF, OFF)
GREEN = Color(OFF, FULL, OFF)
BLUE = Color(OFF, OFF, FULL)

DIM_RED = Color(DIM, OFF, OFF)
DIM_GREEN = Color(OFF, DIM, OFF)
DIM_BLUE = Color(OFF, OFF, DIM)

DARK_RED = Color(DARK, OFF, OFF)
DARK_GREEN = Color(OFF, DARK, OFF)
DARK_BLUE = Color(OFF, OFF, DARK)

CYAN = Color(OFF, FULL, FULL)
MAGENTA = Color(FULL, OFF, FULL)
YELLOW = Color(FULL, FULL, OFF)

DIM_CYAN = Color(OFF, DIM, DIM)
DIM_MAGENTA = Color(DIM, OFF, DIM)
DIM_YELLOW = Color(DIM, DIM, OFF)

DARK_CYAN = Color(OFF, DARK, DARK)
DARK_MAGENTA = Color(DARK, OFF, DARK)
DARK_YELLOW = Color(DARK, DARK, OFF)

DARK_WHITE = Color(DARK, DARK, DARK)
DIM_WHITE = Color(DIM, DIM, DIM)
BLACK = Color(OFF, OFF, OFF)

DIMMEST_WHITE = Color(0.1, 0.1, 0.1)
WHITE = Color(FULL, FULL, FULL)

# endregion

PRIMARIES = [
    RED,
    GREEN,
    BLUE,
]

TWOS = [
    CYAN,
    MAGENTA,
    YELLOW,
]

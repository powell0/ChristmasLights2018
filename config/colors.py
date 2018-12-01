import random
from neopixel import *

# Initialize random number generator
random.seed()

# Predefined colors
OFF         = Color(0,0,0)
WHITE       = Color(255,255,255)
RED         = Color(255,0,0)
GREEN       = Color(0,255,0)
BLUE        = Color(0,0,255)
PURPLE      = Color(128,0,128)
PINK        = Color(255,204,255)
YELLOW      = Color(255,255,0)
ORANGE      = Color(255,50,0)
TURQUOISE   = Color(64,224,208)
BROWN       = Color(165,42,42)

# Generate a random color
def generate_random_color():
    return Color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

COLOR_MAP = {
    "off": OFF,
    "white": WHITE,
    "red": RED,
    "green": GREEN,
    "blue": BLUE,
    "purple": PURPLE,
    "pink": PINK,
    "yellow": YELLOW,
    "orange": ORANGE,
    "turquoise": TURQUOISE,
    "brown": BROWN
}


# Set the context so that parent/sibling packages can be imported
import context

import argparse

from neopixel import Color

from led_strip import *
from config import *

MIN_LED_INDEX = 0
MAX_LED_INDEX = settings.LED_COUNT - 1

def clamp(n, smallest, largest): 
    return max(smallest, min(n, largest))

def try_parse_int(value):
    try:
        return int(value), True
    except ValueError:
        return value, False

def parse_led_identifiers(identifiers):
    indices = []

    for identifier in identifiers:
        result = identifier.split("-", 1)

        if len(result) == 1:
            index, success = try_parse_int(result[0])

            if success:
                index = clamp(index, MIN_LED_INDEX, MAX_LED_INDEX)
                indices.append(index)
            else:
                raise ValueError("%s is not an integer" % result[0])
        else:
            lowerbound, success = try_parse_int(result[0])

            if not success:
                lowerbound = MIN_LED_INDEX

            upperbound, success = try_parse_int(result[1])

            if not success:
                upperbound = MAX_LED_INDEX

            if lowerbound > upperbound:
                lowerbound, upperbound = upperbound, lowerbound

            indices += range(lowerbound, upperbound + 1)

    indices.sort()

    return list(set(indices))

def command_color(led_strip, indices, color_name):
    if color_name == "random":
        color = colors.generate_random_color()
    elif color_name in colors.COLOR_MAP:
        color = colors.COLOR_MAP.get(color_name)

    for i in indices:
        led_strip.strip.setPixelColor(i, color)

    led_strip.strip.show()

def command_components(led_strip, indices, white, red, green, blue):
    color = Color(red, green, blue)
    
    for i in indices:
        led_strip.strip.setPixelColor(i, color)

    led_strip.strip.show()

# Main program logic follows:
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="lights", description="Controls the lights on an LED strip")

    color_names = list(colors.COLOR_MAP.keys())
    color_names.append('random')

    subparsers = parser.add_subparsers(title="subcommands", description='valid subcommands', dest='command_name')
    parser_color = subparsers.add_parser('color', help="Specify light color by name")
    parser_color.add_argument('color', choices=color_names)
    parser_color.add_argument("-i", nargs="*", help="a list of led identifiers or identifier ranges (e.g. 1 3-8 9)")

    parser_components = subparsers.add_parser('components', help="Specifiy light color by component values")
    parser_components.add_argument("-i", nargs="*", help="a list of led identifiers or identifier ranges (e.g. 1 3-8 9)")
    parser_components.add_argument("-w", "--white", type=int, default=0, help="the value of the white component (0-255)")
    parser_components.add_argument("-r", "--red", type=int, default=0, help="the value of the red component (0-255)")
    parser_components.add_argument("-g", "--green", type=int, default=0, help="the value of the green component (0-255)")
    parser_components.add_argument("-b", "--blue", type=int, default=0, help="the value of the blue component (0-255)")

    args = parser.parse_args()

    if args.command_name == None:
        print("Please specify the name of the command to run")
        raise SystemExit(1)
    
    if args.i == None or len(args.i) == 0:
        indices = range(MIN_LED_INDEX, MAX_LED_INDEX + 1)
    else:
        indices = parse_led_identifiers(args.i)

    # Create LedStrip object with default configuration (as defined in config/settings.py)
    led_strip = LedStrip()

    if args.command_name == "color":
        command_color(led_strip, indices, args.color)
        
    elif args.command_name == "components":
        white = clamp(args.white, 0, 255)
        red = clamp(args.red, 0, 255)
        green = clamp(args.green, 0, 255)
        blue = clamp(args.blue, 0, 255)

        command_components(led_strip, indices, white, red, green, blue)

    



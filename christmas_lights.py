import color_model
from config import *
from led_strip import *
import math
from neopixel import Color
import time


# The wait time between led_strip rainbow updates, in ms
# The best way to control how fast it goes is to use the CASCADE_CYCLE_SPEED_FACTOR setting
# which is applied to this time
RAINBOW_UPDATE_WAIT_TIME = 25

rainbow_cascade = []

def _clamp(n, smallest, largest): 
    return max(smallest, min(n, largest))

def create_rainbow_cascade():
    if settings.CASCADE_MODE == 1:
        light_count = int(math.ceil(settings.LED_COUNT / 2))
    else:
        light_count = settings.LED_COUNT

    if settings.BASE_COLOR in colors.COLOR_MAP:
        base_color = colors.COLOR_MAP.get(settings.BASE_COLOR)
    else:
        base_color = colors.OFF

    # Add the initial light states
    rainbow_cascade.extend([base_color for i in range(light_count)])

    # Add rainbow states
    hue_step_repetitions = 1

    # calculate the change in hue for each step ofthe cycle
    hue_step = ((settings.MAX_HUE - settings.MIN_HUE) / (light_count - 1)) / settings.RAINBOW_LENGTH_FACTOR

    # generate a rainbow for each cascade cycle 
    for cycle in range(settings.CASCADE_CYCLES):
        # iterate across the range of hues in the rainbow
        for hue in [i * hue_step for i in range(light_count)]:
            # generate the RGB color values of the rainbow
            r, g, b = color_model.hsl_to_rgb(hue, settings.SATURATION, settings.LUMINOSITY)
            
            rainbow_cascade.append(Color(int(round(255 * r)), int(round(255 * g)), int(round(255 * b))))

    # Add the final light states
    rainbow_cascade.extend([base_color for i in range(light_count)])

def display_rainbow_cascade(led_strip, mode):
    if mode == 1:
        light_count = int(math.ceil(settings.LED_COUNT / 2))
    else:
        light_count = settings.LED_COUNT

    # calculate the delay between updating the lights
    wait = RAINBOW_UPDATE_WAIT_TIME / settings.CASCADE_CYCLE_SPEED_FACTOR

    # iterate through the lower bound index to create a sliding window across
    # the entire rainbow cascade array
    for i in range(len(rainbow_cascade) - light_count + 1):
        # grab the colors from the rainbow cascade that fall within the sliding window
        color_pattern = rainbow_cascade[i:i + light_count]

        if mode == 0:
            # Turn on all the lights with the colors specified in the pattern array, starting from the end of the strand
            start = _clamp(settings.CASCADE_START_POSITION_OFFSET, 0, light_count - 1)
            end = _clamp(light_count - 1 + settings.CASCADE_START_POSITION_OFFSET, 0, light_count - 1)
            color_pattern.reverse()

            led_strip.lightStrip(color_pattern, start, end)
        elif mode == 1:
            # Calculate the positions of the first half of the strand for the first cascade
            first_half_start = 0
            first_half_end = light_count + settings.CASCADE_START_POSITION_OFFSET
            first_half_lights = range(first_half_start, first_half_end)

            # Calculate the positions of the second half of the strand for the second cascade
            second_half_start = first_half_end - (settings.LED_COUNT % 2)
            second_half_end = settings.LED_COUNT
            second_half_lights = range(second_half_start, second_half_end)

            reversed_color_pattern = list(color_pattern)
            reversed_color_pattern.reverse()

            # Set the lights of the first half of the strand
            for position in first_half_lights:
                led_strip.strip.setPixelColor(position, color_pattern[position])

            # Set the lights of the second half of the strand
            for position in second_half_lights:
                led_strip.strip.setPixelColor(position, reversed_color_pattern[position - second_half_start])

            led_strip.strip.show()
        elif mode == 2:
            # Turn on all the lights with the colors specified in the pattern array, starting from the beginning of the strand
            start = _clamp(settings.CASCADE_START_POSITION_OFFSET, 0, light_count - 1)
            end = _clamp(light_count - 1 + settings.CASCADE_START_POSITION_OFFSET, 0, light_count - 1)

            led_strip.lightStrip(color_pattern, start, end)
        elif mode == 3:
            # Turn on all the lights with the same color
            led_strip.allOn(color_pattern[0])
        else:
            # Turn on one light
            led_strip.on(settings.CASCADE_START_POSITION_OFFSET, color_pattern[0])

        time.sleep(wait / 1000.0)

# Main program logic follows:
if __name__ == '__main__':

    # Create LedStrip object with default configuration (as defined in config/settings.py)
    led_strip = LedStrip()

    # Create the rainbow cascade
    create_rainbow_cascade()

    display_rainbow_cascade(led_strip, settings.CASCADE_MODE)

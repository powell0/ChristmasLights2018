
import time

from neopixel import *

from config import settings
from config import colors

def _clamp(n, smallest, largest): 
    return max(smallest, min(n, largest))

class LedStrip:
    def __init__(self, led_count = settings.LED_COUNT, pin = settings.LED_PIN, frequency = settings.LED_FREQ_HZ, dma = settings.LED_DMA, invert = settings.LED_INVERT, brightness = settings.LED_BRIGHTNESS, pwm_channel = settings.LED_PWM_CHANNEL, strip_type = settings.LED_STRIP_TYPE):
        # Create NeoPixel object with appropriate configuration.
        self.strip = Adafruit_NeoPixel(led_count, pin, frequency, dma, invert, brightness, pwm_channel, strip_type)
        self.led_count = led_count

        # Intialize the library (must be called once before other functions).
        self.strip.begin()

    def on(self, pos, color=colors.WHITE):
        """Sets the given pixel to the provided color"""
        pos = _clamp(pos, 0, self.led_count - 1)

        self.strip.setPixelColor(pos, color)

        self.strip.show()

    def off(self, pos):
        """Turns the given pixel off"""
        pos = _clamp(pos, 0, self.led_count - 1)

        self.strip.setPixelColor(pos, colors.OFF)

        self.strip.show()

    def allOn(self, color=colors.WHITE):
        """
        Sets all pixels to the provided color.
        """
        for i in range(self.led_count):
            self.strip.setPixelColor(i, color)

        self.strip.show()

    def allOff(self):
        """
        Turns off all the LEDS.
        """
        for i in range(self.led_count):
            self.strip.setPixelColor(i, colors.OFF)

        self.strip.show()

    def lightStrip(self, color_pattern, startPos=0, endPos=-1):
        """
        Turn on the lights using the specified color pattern
        Can optionally specify a sub segment using the start and end positions
        """
        last_led = self.led_count - 1

        if endPos < 0 or endPos > last_led:
            endPos = led_count

        startPos = _clamp(startPos, 0, last_led)

        if startPos > endPos:
            startPos, endPos = endPos, startPos

        color_pattern_len = len(color_pattern)

        # set the lights to the color pattern given, repeating the colors as neccessary
        for i in range(startPos, endPos + 1):
            self.strip.setPixelColor(i, color_pattern[(i - startPos) % color_pattern_len])

        self.strip.show()

    def blinkNumTimes(self, color=colors.WHITE, numberOfBlinks=1, wait_ms=1000):
        """
        Blinks the strip for the specified number of times.
        Can specify the color and delay between blinks.
        """
        for num in range(0, numberOfBlinks):
            self.allOn(color)

            time.sleep(wait_ms/1000.0)

            self.allOff()

            time.sleep(wait_ms/1000.0)
        
    def colorWipe(self, color, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        for i in range(self.led_count):
            self.strip.setPixelColor(i, color)

            self.strip.show()

            time.sleep(wait_ms/1000.0)

    def theaterChase(self, color, wait_ms=50, iterations=10):
        """Movie theater light style chaser animation."""
        for j in range(iterations):
            for q in range(3):
                for i in range(0, self.led_count, 3):
                    self.strip.setPixelColor(i+q, color)

                self.strip.show()

                time.sleep(wait_ms/1000.0)

                for i in range(0, self.led_count, 3):
                    self.strip.setPixelColor(i+q, 0)

    def _wheel(self, pos):
        """Generate rainbow colors across 0-255 positions."""
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)

    def rainbow(self, wait_ms=20, iterations=1):
        """Draw rainbow that fades across all pixels at once."""
        for j in range(256*iterations):
            for i in range(self.led_count):
                pos = (i+j) & 255
                self.strip.setPixelColor(i, self._wheel(pos))

            self.strip.show()

            time.sleep(wait_ms/1000.0)

    def rainbowCycle(self, wait_ms=20, iterations=5):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for j in range(256*iterations):
            for i in range(self.led_count):
                pos = ((i * 256 / self.strip.numPixels()) + j) & 255
                self.strip.setPixelColor(i, self._wheel(pos))

            self.strip.show()

            time.sleep(wait_ms/1000.0)

    def theaterChaseRainbow(self, wait_ms=50):
        """Rainbow movie theater light style chaser animation."""
        for j in range(256):
            for q in range(3):
                for i in range(0, self.led_count, 3):
                    pos = (i+j) % 255
                    self.strip.setPixelColor(i+q, self._wheel(pos))

                self.strip.show()

                time.sleep(wait_ms/1000.0)

                for i in range(0, self.led_count, 3):
                    self.strip.setPixelColor(i+q, 0)

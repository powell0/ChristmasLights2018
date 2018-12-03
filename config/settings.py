from neopixel import ws 

# LED strip configuration:
LED_COUNT       = 50                   # Number of LED pixels.
LED_PIN         = 18                   # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ     = 800000               # LED signal frequency in hertz (usually 800khz)
LED_DMA         = 5                    # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS  = 255                  # Set to 0 for darkest and 255 for brightest
LED_INVERT      = False                # True to invert the signal (when using NPN transistor level shift)
LED_PWM_CHANNEL = 0                    # PWM channel to use for generating signal (typically 0)
LED_STRIP_TYPE  = ws.WS2811_STRIP_RGB  # The LED Strip type

# RAINBOW CASCADE SETTINGS
BASE_COLOR = "white"                   # The base color of the light strand, options are: "off", "white", "red", "green", "blue", "purple", "pink", "yellow", "orange", "turquoise", and "brown"

CASCADE_MODE = 1                       # The starting position of the cascade 
                                       # 0 = travels from the beginning of the strand to the end
                                       # 1 = travels from the middle of the strand to both ends
                                       # 2 = travels from the end of the strand to the beginning
                                       # 3 = all lights cycle through the rainbow colors
                                       # 4 = one light cycles through the rainbow colors, defined by CASCADE_START_POSITION_OFFSET

CASCADE_START_POSITION_OFFSET = 0      # The number of lights to offset the start position 
                                       # <0 moves the start position closer to the beginning of the strand
                                       # >1 moves the start position closer to the end of the strand

CASCADE_CYCLES = 1                     # The number of times to cycle through the rainbow

CASCADE_CYCLE_SPEED_FACTOR = 1.0       # A multiplier that controls how fast one cascade cycle completes
                                       # Values less than 1.0 slow down the cycle
                                       # Values greater than 1.0 speed the cycle up

RAINBOW_LENGTH_FACTOR = 1.0            # A multiplier that controls how many lights make up complete rainbow. 
                                       # A value of 1.0 makes the rainbow the same length as the number of lights the rainbow travels down
                                       # Values less than 1.0 compress the rainbow
                                       # Values greater than 1.0 stretch the rainbow

MIN_HUE    = 0                         # Minimum Hue in the rainbow (0 = Red)
MAX_HUE    = 300                       # Maximum Hue in the rainbow (300 = Magenta)
SATURATION = 1.0                       # 0.0 to 1.0
LUMINOSITY = 0.5                       # 0.0 to 1.0

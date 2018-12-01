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


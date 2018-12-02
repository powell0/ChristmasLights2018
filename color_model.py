
def _clamp(n, smallest, largest): 
    return max(smallest, min(n, largest))

def hsl_to_rgb(hue, saturation, luminosity):
    hue = _clamp(hue, 0, 360)
    saturation = _clamp(saturation, 0.0, 1.0)
    luminosity = _clamp(luminosity, 0.0, 1.0)

    chroma = (1 - abs(2*luminosity - 1)) * saturation

    scaled_hue = hue / 60

    intermediate_component = chroma * (1 - abs((scaled_hue % 2) - 1))

    luminosity_offset = luminosity - (chroma / 2)

    red = luminosity_offset
    green = luminosity_offset
    blue = luminosity_offset

    if scaled_hue <= 1:
        red += chroma
        green += intermediate_component
        blue += 0
    elif scaled_hue <= 2:
        red += intermediate_component
        green += chroma
        blue += 0
    elif scaled_hue <= 3:
        red += 0
        green += chroma
        blue += intermediate_component
    elif scaled_hue <= 4:
        red += 0
        green += intermediate_component
        blue += chroma
    elif scaled_hue <= 5:
        red += intermediate_component
        green += 0
        blue += chroma
    else:
        red += chroma
        green += 0
        blue += intermediate_component

    return red, green, blue

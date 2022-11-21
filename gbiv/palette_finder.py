"""
Author:               Ian McConachie, Sam Heilenbach, Scott Wallace
Team:                 DUX D-Zine
Class:                CS 422
Professor:            Juan Flores, Kartikeya Sharma
Date Created:         11/09/2022
Date Last Modified:   11/21/2022

This is a python script for extracting the dominant color from an
image and creating a palettes. This script was written for the purpose
of the Gbiv project by DUX D-Zine.

"""

## IMPORT STATEMENTS

from colorthief import *
from colorsys import *


## HELPER FUNCTIONS

def tup_to_dict(tup):
    #tuple to dict with index as key
    retDict = {}
    i = 0

    for x in tup:
        retDict[str(i)] = x
        i += 1

    return retDict

def rgb_to_hex(rgb):
    """
    This function converts a tuple of integer values [0, 255] representing a
    color in rgb format to hexadecimal format.

    :inputs:  This function has a single input which is a tuple of
              length 3 with integers 
    :returns: This function returns a string which is the color in
              hexdecimal format.
    """
    hex_str = "%02x%02x%02x" % (rgb[0], rgb[1], rgb[2])

    return hex_str


def rgb_to_percents(rgb):
    """
    This function takes rgb tuple values ranging from 0 to 255 and converts
    them to percent rgb tuple values ranging from 0.0 to 1.0.

    :inputs:  There is a single argument which is a tuple of length 3 with
              integer values ranging from 0 to 255
    :returns: This function returns a single value which is a tuple of length
              3 with each value in the tuple being a float ranging from
              0.0 to 1.0.
    """
    tup = ((rgb[0]/255), (rgb[1]/255), (rgb[2]/255))

    return tup


def hls_to_hex(hls):
    """
    This function takes an hls tuple of length 3 and converts it into 
    hexadecimal form.

    :inputs:  This function takes one argument: a tuple of length 3 with hls
              values in a range from 0.0 to 1.0
    :returns: The return value of this function is the hexadecimal 
    """

    # Make hls values into rgb percent values
    rgb_pers = hls_to_rgb(hls[0], hls[1], hls[2])

    # Convert rgb percent values to hexadecimal strings
    rgb = (round(rgb_pers[0]*255), round(rgb_pers[1]*255), round(rgb_pers[2]*255))
    hexa = rgb_to_hex(rgb)

    return hexa


## PALETTE FUNCTIONS

# Monochromatic Palettes

def mono_up(hls):
    """
    This function generates a palette that is monochromatic and has shades that
    vary from the inputted color to white. Each subsequent hue is lighter than
    the previous color.

    :inputs:  This function takes a single input which is a tuple of length 3
              which describes the color in hls format with float values
              ranging from 0.0 to 1.0
    :returns: This function returns a tuple of strings, each representing a 
              color in the generated palette, of which there are 4.
    """

    # Focusing on luminosity
    lum = hls[1]

    # Create palette
    increment = ((1-lum)/3)
    color2 = (hls[0], (hls[1]+ increment), hls[2])
    color3 = (hls[0], (lum + (2*increment)), hls[2])
    color4 = (hls[0], 1.0, hls[2])

    # Convert hls values to hexadecimal and format as tuple
    tup = (hls_to_hex(hls), hls_to_hex(color2), hls_to_hex(color3), hls_to_hex(color4))

    return tup_to_dict(tup)


def mono_down(hls):
    """
    This function generates a palette that is monochromatic and has shades that
    vary from the inputted color to black. Each subsequent hue is darker than 
    the previous color

    :inputs:  This function takes a single input which is a tuple of length 3
              which describes the color in hls format with float values
              ranging from 0.0 to 1.0
    :returns: This function returns a tuple of strings, each representing a 
              color in the generated palette, of which there are 4.
    """


    # Focusing on luminosity
    lum = hls[1]

    # Create palette
    decrement = (lum/3)
    color2 = (hls[0],(lum - decrement), hls[2])
    color3 = (hls[0], (lum - (2*decrement)), hls[2])
    color4 = (hls[0], 0.0, hls[2])

    # Convert hls values to hexadecimal and format as tuple
    tup = (hls_to_hex(hls), hls_to_hex(color2), hls_to_hex(color3), hls_to_hex(color4))

    return tup_to_dict(tup)


# Analogous Palettes

def get_analogous_right(dom):
    """
    This function returns an array of 2 analogous colors to the right side of a given dominant color on the color wheel.
    ex: apple red would return red-orange and pumpkin orange
    """
    rgb = rgb_to_percents(dom)
    dom_hls = rgb_to_hls(rgb[0], rgb[1], rgb[2])

    analogous = []

    color1 = (dom_hls[0]+.025, dom_hls[1], dom_hls[2])
    color2 = (dom_hls[0]+.05, dom_hls[1], dom_hls[2])
    color3 = (dom_hls[0]+.075, dom_hls[1], dom_hls[2])

    color1 = hls_to_hex(color1)
    color2 = hls_to_hex(color2)
    color3 = hls_to_hex(color3)

    analogous.append(color1)
    analogous.append(color2)
    analogous.append(color3)

    return (analogous[0], analogous[1], analogous[2])


def get_analogous_left(dom):
    """
    This function returns an array of 3 analagouos colors to the left side of a given dominant color on the color wheel.
    ex: apple red would return a magenta and violet shade
    """
    rgb = rgb_to_percents(dom)
    dom_hls = rgb_to_hls(rgb[0], rgb[1], rgb[2])

    analogous = []

    color1 = (dom_hls[0]-.025, dom_hls[1], dom_hls[2])
    color2 = (dom_hls[0]-.05, dom_hls[1], dom_hls[2])
    color3 = (dom_hls[0]-.075, dom_hls[1], dom_hls[2])

    color1 = hls_to_hex(color1)
    color2 = hls_to_hex(color2)
    color3 = hls_to_hex(color3)

    analogous.append(color1)
    analogous.append(color2)
    analogous.append(color3)


    return (analogous[0], analogous[1], analogous[2])


def get_analogous_centered(dom):
    """
    This function returns an array of 2 analagouos colors to the left side of a given dominant color on the color wheel 
    and two to the right of the dominant color.
    ex: apple red would return a magenta and violet shade as well as a red-orange and pumpkin orange
    """
    rgb = rgb_to_percents(dom)
    dom_hls = rgb_to_hls(rgb[0], rgb[1], rgb[2])

    analogous = []

    color1 = (dom_hls[0]-.025, dom_hls[1], dom_hls[2])
    color2 = (dom_hls[0]-.05, dom_hls[1], dom_hls[2])
    color3 = (dom_hls[0]+.025, dom_hls[1], dom_hls[2])
    color4 = (dom_hls[0]+.05, dom_hls[1], dom_hls[2])

    color1 = hls_to_hex(color1)
    color2 = hls_to_hex(color2)
    color3 = hls_to_hex(color3)
    color4 = hls_to_hex(color4)

    analogous.append(color1)
    analogous.append(color2)
    analogous.append(color3)
    analogous.append(color4)



    return (analogous[0], analogous[1], analogous[2], analogous[3])

# Complimentary Palettes

def get_complimentary(dom):
    """
    This function returns an array of 3 complimentary colors given a dominant color.
    """
    rgb = rgb_to_percents(dom)
    dom_hls = rgb_to_hls(rgb[0], rgb[1], rgb[2])

    complimentary = []

    color1 = (dom_hls[0]+.5, dom_hls[1], dom_hls[2])
    color2 = (color1[0]-.025, color1[1], color1[2])
    color3 = (color1[0]-.05, color1[1], color1[2])
    color4 = (color1[0]+.025, color1[1], color1[2])
    color5 = (color1[0]+.05, color1[1], color1[2])

    color1 = hls_to_hex(color1)
    color2 = hls_to_hex(color2)
    color3 = hls_to_hex(color3)
    color4 = hls_to_hex(color4)
    color5 = hls_to_hex(color5)

    complimentary.append(color1)
    complimentary.append(color2)
    complimentary.append(color3)
    complimentary.append(color4)
    complimentary.append(color5)

    
    return (complimentary[0], complimentary[1], complimentary[2], complimentary[3], complimentary[4])




## PRIMARY FUNCTIONS

def color_extractor(path):
    """
    This function extracts the dominant color from an image uploaded by the
    user.

    :inputs:  This function takes a single input which is a path (in the 
              form of a string) to the image we wish to extract the dominant
              color from.
    :returns: This function returns a tuple where the first value is a string
              with the hex value of the dominant color and the second value
              is a tuple with 3 values representing the rgb formatting of the
              color.
    """

    # Extract dominant color
    ct = ColorThief(path)
    dom = ct.get_color(quality=1)

    # Convert rgb output from ColorThief to hex value
    hex_val = rgb_to_hex(dom)

    return (hex_val, dom)


def palette_generator(dom):
    """
    This function generates a palette of 4 colors from a single dominant color
    that has 
    """

    # Converting rgb to hls tuple
    rgb = rgb_to_percents(dom)
    dom_hls = rgb_to_hls(rgb[0], rgb[1], rgb[2])

    # Generating monochromatic palettes
    mono_u = mono_up(dom_hls)
    mono_d = mono_down(dom_hls)

    return (mono_u, mono_d)



def main():
    path = "static/images/red.png"
    (hexa, rgb) = color_extractor(path)
    palettes = palette_generator(rgb)
    print()
    print("Dominant Color:             ", hexa)
    print("Monochromatic Up Palette:   ", palettes[0])
    print("Monochromatic Down Palette: ", palettes[1])
    print()

if __name__ == "__main__":
    main()

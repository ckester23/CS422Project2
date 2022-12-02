"""
Author:               Ian McConachie, Sam Heilenbach, Scott Wallace
Team:                 DUX D-Zine
Class:                CS 422
Professor:            Juan Flores, Kartikeya Sharma
Date Created:         11/09/2022
Date Last Modified:   12/02/2022

This is a python script for extracting the dominant color from an
image and creating a palettes. This script was written for the purpose
of the Gbiv project by DUX D-Zine.

"""

## IMPORT STATEMENTS

from colorthief import *
from colorsys import *


## HELPER FUNCTIONS

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

    return tup 


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

    return tup


# Analogous Palettes

def get_analogous_right(dom):
    """
    This function returns an array of 2 analogous colors to the right side of a given dominant color on the color wheel.
    ex: apple red would return red-orange and pumpkin orange
    """

    color1 = ((dom[0]+.025)%1, dom[1], dom[2])
    color2 = ((dom[0]+.05)%1, dom[1], dom[2])
    color3 = ((dom[0]+.075)%1, dom[1], dom[2])

    analogous = (hls_to_hex(dom), hls_to_hex(color1), hls_to_hex(color2), hls_to_hex(color3))

    return analogous



def get_analogous_left(dom):
    """
    This function returns an array of 3 analagouos colors to the left side of a given dominant color on the color wheel.
    ex: apple red would return a magenta and violet shade
    """

    color1 = ((dom[0]-.025)%1, dom[1], dom[2])
    color2 = ((dom[0]-.05)%1, dom[1], dom[2])
    color3 = ((dom[0]-.075)%1, dom[1], dom[2])

    analogous = (hls_to_hex(dom), hls_to_hex(color1), hls_to_hex(color2), hls_to_hex(color3))


    return analogous


# Tetradic Palettes


def rectangular_right(hls):
    """
    This function generates a palette that is has a rectangular tetradic color
    palette. This means it has the base color, the color that is 60 degrees
    to the right on the color wheel,  the color that is 180 degrees to the
    right on the color wheel, and the color that is 240 degrees to the right
    on the color wheel.

    :inputs:  This function takes a single input which is a tuple of length 3
              which describes the color in hls format with float values
              ranging from 0.0 to 1.0
    :returns: This function returns a tuple of strings, each representing a 
              color in the generated palette, of which there are 4.
    """


    # Focusing on hue
    hue = hls[0]

    # Create palette
    color2 = (hue+(1/6),hls[1], hls[2])
    color3 = (hue+(1/3), hls[1], hls[2])
    color4 = (hue+(1/6), hls[1], hls[2])

    # Convert hls values to hexadecimal and format as tuple
    tup = (hls_to_hex(hls), hls_to_hex(color2), hls_to_hex(color3), hls_to_hex(color4))

    return tup


def rectangular_left(hls):
    """
    This function generates a palette that is has a rectangular tetradic color
    palette. This means it has the base color, the color that is 60 degrees
    to the right on the color wheel,  the color that is 180 degrees to the
    right on the color wheel, and the color that is 240 degrees to the right
    on the color wheel.

    :inputs:  This function takes a single input which is a tuple of length 3
              which describes the color in hls format with float values
              ranging from 0.0 to 1.0
    :returns: This function returns a tuple of strings, each representing a 
              color in the generated palette, of which there are 4.
    """


    # Focusing on hue
    hue = hls[0]

    # Create palette
    color2 = (hue-(1/6),hls[1], hls[2])
    color3 = (hue-(1/3), hls[1], hls[2])
    color4 = (hue-(1/6), hls[1], hls[2])

    # Convert hls values to hexadecimal and format as tuple
    tup = (hls_to_hex(hls), hls_to_hex(color2), hls_to_hex(color3), hls_to_hex(color4))

    return tup

## Functions NOT Integrated Yet ##

def get_analogous_centered(dom):
    """
    This function returns an array of 2 analagouos colors to the left side of a given dominant color on the color wheel 
    and two to the right of the dominant color.
    ex: apple red would return a magenta and violet shade as well as a red-orange and pumpkin orange
    """

    color1 = ((dom[0]-.025), dom[1], dom[2])
    color2 = ((dom[0]-.05), dom[1], dom[2])
    color3 = ((dom[0]+.025), dom[1], dom[2])
    color4 = ((dom[0]+.05), dom[1], dom[2])

    tup = (hls_to_hex(color1), hls_to_hex(color2), hls_to_hex(color3), hls_to_hex(color4))

    return tup


# Complimentary Palettes

def get_complimentary(dom):
    """
    This function returns an array of 3 complimentary colors given a dominant color.
    """

    color1 = ((dom[0]+.5)%1, dom[1], dom[2])
    color2 = ((color1[0]-.025)%1, color1[1], color1[2])
    color3 = ((color1[0]-.05)%1, color1[1], color1[2])
    color4 = ((color1[0]+.025)%1, color1[1], color1[2])
    color5 = ((color1[0]+.05)%1, color1[1], color1[2])

    tup = (hls_to_hex(color1), hls_to_hex(color2), hls_to_hex(color3), hls_to_hex(color4), hls_to_hex(color5))

    return tup




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
    anlg_r = get_analogous_right(dom_hls)
    anlg_l = get_analogous_left(dom_hls)
    rect_r = rectangular_right(dom_hls)
    rect_l = rectangular_left(dom_hls)

    return ("Monochromatic", mono_u, mono_d, "Analogous", anlg_r, anlg_l, "Tetradic", rect_r, rect_l)


def related_colors_generator(dom):
    """
    This function generates a palette of 4 colors from a single dominant color
    that has 
    """

    # Converting rgb to hls tuple
    rgb = rgb_to_percents(dom)
    dom_hls = rgb_to_hls(rgb[0], rgb[1], rgb[2])

    # Generating monochromatic palettes
    compl = get_complimentary(dom_hls)
    analg = get_analogous_centered(dom_hls)

    return ("relcolors", "Complimentary", compl, "Shades", analg)



def main():
    path = "static/images/red.png"
    (hexa, rgb) = color_extractor(path)
    palettes = palette_generator(rgb)
    print()
    print("Dominant Color:             ", hexa)
    print("Monochromatic Up Palette:   ", palettes[0])
    print("Monochromatic Down Palette: ", palettes[1])
    print("Analogous Right Palette: ", palettes[2])
    print("Analogous Left Palette: ", palettes[3])
    print()

if __name__ == "__main__":
    main()

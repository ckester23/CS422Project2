"""
Author:               Cheyanne Kester
Team:                 DUX D-Zine
Class:                CS 422
Professor:            Juan Flores, Kartikeya Sharma
Date Created:         11/20/2022
Date Last Modified:   11/20/2022

This provides functions to parse palette STRINGS of the form
    "({'0': 'a27ea2', '1': 'c1a9c1', '2': 'e0d4e0', '3': 'ffffff'}, 
    {'0': 'a27ea2', '1': '705070', '2': '382838', '3': '000000'})"
into python LISTS, so that we can utilize the values for display
"""

"""
<div class="card" style="width: 18rem;">
	<img class="card-img-top" src="\static\images\solid-color-image.png" alt="Card image cap">
	<div class="card-body">
	  <h5 class="card-title">{{palettes[1:61]}}</h5>
	</div>
</div>
"""

def parseListOfPalettes(pList: str):
    """
    """
    palette1 = pList[1:61]
    palette2 = pList[63:123]

    parsedPalette1 = parsePalette(palette1)
    parsedPalette2 = parsePalette(palette2)

    return [parsedPalette1, parsedPalette2]


def parsePalette(pal: str):
    """
    """
    color1 = '#' + pal[7:13]
    color2 = '#' + pal[22:28]
    color3 = '#' + pal[37:43]
    color4 = '#' + pal[52:58]

    return [color1, color2, color3, color4]



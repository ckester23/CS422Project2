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

def parsePalette(httpStr):
    colorList = []
    color = ''
    append = False

    for s in httpStr:
        if s.isalnum():
            color += s
            append = True
        elif(append):
                colorList.append(str(color))
                color = ''
                append = False

    return colorList 

if __name__ == "__main__":
    print(parsePalette("(('cc242c', 'e4666c', 'f1b3b5', 'ffffff'), ('cc242c', '88181d', '440c0f', '000000'), ('cc242c', 'cc3524', 'cc4e24', 'cc6824'), ('cc242c', 'cc2445', 'cc245e', 'cc2478'))"))

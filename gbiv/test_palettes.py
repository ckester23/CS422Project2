"""
Author:               Sam Heilenbach
Team:                 DUX D-Zine
Class:                CS 422
Professor:            Juan Flores, Kartikeya Sharma
Date Created:         11/29/2022
Date Last Modified:   12/02/2022

This is a python script for testing the functionality in the palette_finder.py module.
This script was written for the purpose of the Gbiv project by DUX D-Zine.

"""
from palette_finder import * 
import pytest


img_path = './static/test_red.png'
img_hsl = (.03, .77, .50)
img_rgb = (224, 38, 29)
img_hex = ("e0261d")

img2_path = './static/test_blue.png'
img2_hsl = (.63, .65, .49)
img2_rgb = (44, 71, 204)
img2_hex = '2c47cc'

class TestMain:
	### Testing the primary functionality of the color extraction/palette generator ###

	def test_rgb_to_hex(self):
		assert rgb_to_hex(img_rgb) == img_hex

	###FOR FUTURE DEVELOPMENT###
	# def test_hls_to_rgb(self):
	# 	rgb = hls_to_rgb(img_hsl[0], img_hsl[1], img_hsl[2])
	# 	print(hls_to_rgb(img_hsl[0], img_hsl[1], img_hsl[2]))
	# 	assert  (rgb[0]*255, rgb[1]*255, rgb[2]*255) == img_rgb

	# def test_hsl_to_hex(self):
	# 	assert hls_to_hex(img2_hsl) == img2_hex

	def test_extract_dom(self):
		color1 = color_extractor(img_path)
		rgb1 = color1[1]
		color2 = color_extractor(img_path)
		rgb2 = color2[1]
		assert rgb1 == rgb2

	def test_extract_dom_diff(self):
		assert color_extractor(img_path) != color_extractor(img2_path) 


	def test_mono_up_and_down(self):
		mono_u = mono_up(img_hsl)
		mono_d = mono_down(img_hsl)
		assert mono_u[0] == mono_d[0]

	def test_mono_diff(self):
		mono_blue = mono_up(img2_rgb)
		mono_red = mono_up(img_rgb)
		assert mono_blue[0] != mono_red[0]
		assert mono_blue[3] == mono_red[3]

	def test_analogous(self):
		analogous_l = get_analogous_left(img2_hsl)
		analogous_r = get_analogous_right(img2_hsl)
		print(analogous_l)
		assert analogous_r[0] == analogous_l[0]


	###FOR FUTURE DEVELOPMENT###
	# def test_analgous_centered(self):
	# 	analogous_centered = get_analogous_centered(img2_rgb)
	# 	print(analogous_centered)
	# 	analagous_r = get_analogous_right(img2_hsl)
	# 	analagous_l = get_analogous_left(img2_hsl)
	# 	print(analagous_l)
	# 	assert analogous_centered[0] == analagous_l[1]
	# 	assert analogous_centered[2] == analogous_r[1]

	def test_analogous_diff(self):
		analogous_l = get_analogous_left(img_hsl)
		analogous_r = get_analogous_right(img_hsl)
		assert analogous_r[1] != analogous_l[1]

	def test_complimentary(self):
		comp1 = get_complimentary(img_hsl)
		comp2 = get_complimentary(img_hsl)
		assert comp1[0] == comp2[0]

	def test_compilimentary_diff(self):
		comp_blue = get_complimentary(img2_hsl)
		comp_red = get_complimentary(img_hsl)
		assert comp_blue != comp_red





if __name__ == "__main__":
    main()



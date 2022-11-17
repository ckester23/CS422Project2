Specific Requirements
======================


External Interfaces (Inputs and Outputs)
-----------------------------------------


User Image Uploads (Input)
#############################

The user will be able to upload an image to Gbiv in order to extract its dominant color. This is the most important input of the application because it allows users to access the main functionality which is to apply color theory to colors found in the physical world. The photo may be formatted as a .png or a .jpg file and will be restricted to a range of 0 to 99MB.


Palette Filter Selection (Input)
#################################

Users will have the ability to filter what palettes are displayed on two separate pages of Gbiv. They can do this for generated palettes after they have uploaded an image, but also on the example palettes page. This input will have discrete and pre-defined choices which will be selected using principles of color theory. 


Generated Palettes (Output)
###########################

After uploading an image to be analyzed, our application will generate several palettes that contain the dominant color in the image. These palettes will be composed of 4 separate colors and users will have the option to change what palettes are displayed by selecting from provided filter tags. Along with the visual output of these four colors, the corresponding hex codes will also be available to end-users. The output will reach the user through our frontend by way of the website UI. Palettes will be displayed as rectangles divided into 4 horizontal bars each filled with one color from the generated palette. Users will be able to view the hex codes of the colors by hovering their mouse over the palette they are interested in.


Related Colors (Output)
##########################

Similar to outputted palettes, after a user uploads an image Gbiv will calculate colors based on the extracted dominant color. These colors will be related to the user's color based on principles of color theory which will be explained further in the design specification as well as our site's "color theory" page.

These outputs will come from the backend in a similar format as the palettes, but will be displayed on the website in a different fashion. Instead of a single block with several stripes of color, the related colors will be displayed as squares that are filled entirely with a single color. These squares will be grouped in a logical fashion based on color theory fundamentals and like the palettes, will display their hex codes when hovered over.



Functions
----------


Color Extractor
################

This function is the first function that will be called when the user uploads an image. It will be a fairly straightforward function that will take an image as an input (either .jpg or .png) and output the most prominent color in the picture (represented as a hex string). One key component of this function is that it must output in the appropriate format. There are several ways to digitally represent colors and it is vital that we have an output that can be easily translated between different color formats.

Generate Palettes
###################

This function will act as a kind of "main" function that will be called in order to execute several palette creator functions. The generate palette function will pass the dominant color into these functions and save the outputted palettes. After several palettes have been created, the generate palettes function will return the set of sets to be displayed on the user interface.

Palette Creator
$$$$$$$$$$$$$$$$$

This is not a single function, but rather a class of functions that all serve a similar purpose. Each of these functions will take a single color as an input (which will be the color extracted from the user's image) and will output a palette of 4 colors--with one being the inputted color. We will need several of these functions in order to create several types of color-theory-based palettes such as monochromatic, complementary, analogous, and more.


Generate Related Colors
#########################

This function acts in a similar way to the "Generate Palette" function in that it will call several sub-functions and output their combined results in a convenient data format. The sub-functions here are the "Related Color Finder" functions which will take an input of a single color and output several related colors. The "Generate Related Colors" function will then pass the resulting colors to be properly displayed in the frontend.


Related Color Finder
$$$$$$$$$$$$$$$$$$$$$$

This is a class of functions that will each take a single color as an input and output a set of colors that are related based on one particular tenet of color theory. There are a variety of defined color relationships in design, so these functions will be separated based on these relationships to maintain modularity and simplicity.


Usability Requirements
-----------------------

As an application built specifically for design, it is paramount that our site has a well-designed interface. The target users for this application include everyone who has a hand in any kind of design, so people visiting Gbiv will have a range of technical experience and knowledge. To address this, we will have an intuitive user interface that will be supplemented by thorough user documentation. We will also ensure that the site is easily navigable and sufficient information is provided regarding how the colors and palettes are created.


Performance Requirements
--------------------------

Our process of generating relevant palettes and related colors involves doing lots of math with numerical representations of colors. Complex mathematical equations can often be a bottle-neck for web applications, so we are aiming to optimize these functions as much as possible.

We plan to have performance of certain functions fall within defined bounds. Specifically: we plan to have the related colors and color palettes load within 20 seconds 95% percent of the time and we want all website pages to load within 5 seconds of the user clicking on them or visiting the URL.


Software System Attributes 
---------------------------

Due to the diverse backgrounds of the user base we are targeting, two key system attributes we plan to build into Gbiv are usability and portability. We will achieve usability by having an intuitive user interface and thorough documentation that guides users through using the app. We will achieve portability by having the application web-hosted which will allow anyone with a web browser to use Gbiv. Furthermore, we will be building the frontend using Bootstrap which allows for the possibility of a responsive site that will work on a variety of device sizes.

A secondary system attribute that will be kept in mind during the design phase is aesthetics. Because our site is providing a service related to design, having a well-designed site adds to our credibility. This system attribute will be secondary to having an operational and fluid site, but still is important to consider for this particular project.

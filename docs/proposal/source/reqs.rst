Concept of Operations (Basic Requirements) 
============================================

Current System
----------------

There are generally two types of websites that exist today with functionality similar to our application. On one hand, there are sites such as Canva and Adobe Color Extractor which take user uploaded photos and generates a palette that matches the colors in the picture. Alternatively, there are sites like Coolors and MyColorSpace that allow the user to choose a hex color and view color palettes that have that hex color in them. 


Justification For New System
-----------------------------

Design and color theory are everywhere from web development to fashion to interior design and architecture. No existing site has the functionality of our application which provides a powerful tool for applying color theory to the real world. We often have physical items such as paint, clothes, or furniture where we cannot simply check the hex code of the dominant color. Our application combines this analysis of the color in terms of hex along with recommendations for colors to combine it with based on color theory.


Operational Features of Proposed System
----------------------------------------

The operational features of this proposed system will center around what happens after a user has uploaded an image. First a dominant color will be extracted from the photo and displayed to the user. In addition to this, the site will generate several colors that are related to the dominant color by way of color theory. The final output will be a collection of palettes that have the dominant color in it or are in some way adjacent to the color.


User Classes
-------------

Our application will have a single user class which will be designers of all skill levels who are looking to apply color theory in their design choices. This could be users looking for specific color relationships to something they already have (e.g. a color that complements their green wall) or users who are looking for palettes to inspire overall color schemes. The beauty of our application is that it appeals to professional designers by providing a crucial service in a convenient way, as well as the designer in the everyday person by introducing color theory and providing a fun way to experiment with colors.


Modes of Operation
--------------------

There will be a single mode of operation for all regular users of our application. This mode of operation is entered when they visit our site and end up on the main page where photos can be uploaded. On top of this, our team as developers will have a mode of operation where we can upload new palettes and tweak the code for new releases.


Operational Scenarios
-----------------------

Scenario 1
#############

**Uploading an Image**

The user who wishes to extract colors from something tangible in the world, such as a piece of clothing, a building, nature, etc. would want to utilize the Image Upload feature. Upon uploading their selected image, our program will compute a single hex color that occurs most in the image, and captures the general essence of the image. Using this color, our program will then compile a list of color palettes, and another list of related palettes that might not necessarily use the initial color, that the user can view. 



Scenario 2
#############

**Selecting Related Colors and/or Palettes**

Any user who wishes to browse through our page of palettes can view a main list of palettes as an archive, or they may enter or select a specific color, and view palettes that work with that color, as well as related palettes.
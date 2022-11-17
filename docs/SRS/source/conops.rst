

The Concept of Operations (ConOps)
===================================


Current System
----------------

There are generally two types of web applications that exist today with functionality similar to Gbiv. On one hand, there are sites such as Canva and Adobe Color Extractor which take user uploaded photos and generate a palette that matches the colors in the picture [:ref:`1<cite-1>`, :ref:`2<cite-2>`]. Alternatively, there are sites like Coolors and ColorSpace that allow the user to choose a color (by entering a hex code) and view color palettes that contain the hue [:ref:`3<cite-3>`, :ref:`4<cite-4>`]. 

Because color theory is a well known practice in design, there are many more sites that aim to help people choose and analyze colors and color palettes. Many of these applications have use cases adjacent to what Gbiv offers, but currently there is no website that allows users to extract the dominant color from an image and have palettes and related colors recommended.


Justification for a New System
-------------------------------

Color design is everywhere from web development to fashion to interior design and architecture. We often have physical items such as paint, clothes, or furniture where we cannot simply check the hex code to see its color. Gbiv allows users to find the dominant color (in terms of hex) from any image and goes even further by recommending color combinations and palettes based on color theory.

There is a large need for such a system because of the ubiquity of color matching decisions. Of course the designers of the world often need such tools, but there exists hundreds of everyday situations where Gbiv would come in handy for those of us who are not necessarily professionals. Whether you are deciding what pants to wear with your new shirt, repainting the living room, or buying a new couch: color matters. With Gbiv, we will use the science of color to help you make informed design choices without having to study color theory for years.


Operational Features of the Proposed System
---------------------------------------------

The operational features of this proposed system will center around what happens after a user has uploaded an image. First a dominant color will be extracted from the photo and displayed to the user. The site will then  output several color palettes that contain this color which will be generated using principles of color theory. Simultaneously, Gbiv will suggest several individual related colors that may also be of use when making design decisions in the physical world. 

Beyond this primary function, Gbiv will provide example palettes that can be sorted based on certain features of the colors such as whether the palettes are complementary, monochrome, analogous, etc. On other pages information about color theory that will help users to understand the science behind the application's palettes and suggested colors.


User Classes
-------------


Our application will have a single user class which will be designers of all skill levels. This could be people looking for specific color relationships to something they already have (e.g. a color that complements their green wall) or users who are looking for palettes to inspire overall color schemes. The beauty of our application is that it appeals to professional designers by conveniently providing a crucial service, as well as your everyday consumer. Gbiv will introduce color theory and provide an intuitive user experience that will allow color experimentation and education without the need for formal design education.


Modes of Operation
-------------------

There will be a single mode of operation for all regular users of our application. This mode of operation is entered when they visit our site and end up on the main page where photos can be uploaded. In this state, users can navigate around the site and find all the information and functionality provided by Gbiv. 

On top of this, our team as developers will have a mode of operation where we can upload new palettes and tweak the code for new releases. For now, only members of DUX D-Zine will be able to enter this mode of operation, but in the future Gbiv could be made open source and opened up for contribution from the community. 


Operational Scenarios 
--------------------------

Scenario 1
#############

**Uploading an Image**

**Brief Description:** 

This use case describes how a user would upload an image to Gbiv in order to trigger the color analysis that is the primary functionality of the website.

**Actors:** 

A user

**Preconditions:**

1. The user must have a browser that satisfies the requirements necessary to access the Gbiv site.
2. The user must visit Gbiv's URL through their browser.

**Steps to Complete the Task:**

1. The user selects "Upload Image" on the gray rectangle at the top of the screen
2. A file system GUI will open up where they will be able to select a file to upload
3. The user will select a file that is properly formatted (**NOTE:** Gbiv will accept both .png and .jpg files, but no other image file types)
4. If the input is accepted, Gbiv's analysis and suggestion procedure will begin

**Postconditions**

The site will now display the dominant color that has been extracted from the image. Below the dominant color, several palettes will be displayed once the color processing has been completed. Once the palettes area is ready to be populated, related colors will also be displayed below the palette section.



Scenario 2
#############

**Viewing Example Palettes**


**Brief Description:** 

This use case describes how a user would go about viewing example palettes on Gbiv.


**Actors:** 

A user

**Preconditions:**

1. The user must have a browser that satisfies the requirements necessary to access the Gbiv site.
2. The user must visit Gbiv's URL through their browser.


**Steps to Complete the Task:**

1. User first will click on the "Example Palettes" tab on the navbar to go to the palettes page. When they first follow the link, the page will be populated with a default mix of the available palette examples.
2. On the top portion of the page there will be several buttons labeled with particular tags for palettes. At the start all of them will not be selected.
3. The user can then click the tag they wish to use to filter the examples.
4. The page will refresh and display a different set of example palettes that match the selected tag. The user can view all of the palettes by scrolling through the page and the hex codes for the individual colors by hovering their mouse over the color blocks.


**Postconditions**

After completing this use case, users will have access to several example palettes that meet their specified category requirements. They will be able to see these palettes visually and access the hex codes for each individual color if they so choose.
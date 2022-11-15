Software Modules
=================

Frontend Manager
-----------------


Backend Manager
-----------------


Web Interface
---------------


Main Page (Upload an Image)
#############################


Popular Palettes Page
#######################


Color Theory Page
##################


About Us Page
################




Color Analysis
-------------------

The primary function of this module is to the color analysis and generation that happens after a user has uploaded a photo. This module is made up of several sub-modules (divided by functionality) which are further divided into sub-sub modules. The static model below gives a visual picture of how the color analysis module is structured.


.. figure:: images/color_analyzer_static.png
   :name: color-analyzer-static
   :scale: 50%

   Color Analysis Module Static Model


As the above model shows, essentially all of the work with color manipulation and analysis is done within the module. This makes for a high level of cohesion that allows for a weak coupling with other modules in the system. In fact, the color analysis module only has to interact with a single module which is the "Backend Manager." The backend manager passes an image in the form of a .png, .jpg, or .jpeg file and this module returns several sets of color codes as lists of hex code strings. The inter-module interactions of this part of the system are further specified in the dynamic model below.


.. figure:: images/color_analyzer_dynamic.png
   :name: color-analyzer-dynamic
   :scale: 50%

   Color Analysis Module Dynamic Model


This module was designed with a high degree modularity in mind. By separating the color analysis process into two parts, we are able to define two classes of sub-functions that share common features: palette generator functions and related color finder functions. This allows for code re-use and also source code that is easier to read and interpret. We also designed this module to have simple data types as both inputs and outputs. This allows easier integration with the rest of the system and fits well into our chosen framework (Flask).


Palette Database
------------------

The purpose of the Palette Database module will be to store popular palettes that many visitors to Gbiv have looked at. This will allow users to view a range of different color combinations and get inspiration for their design projects. Because there is only one collection of elements in the database for this project, the design of the database itself is somewhat straightforward. The static model below shows the layout visually:

.. figure:: images/palette_database_static.png
   :name: palette-database-static
   :scale: 50%

   Palette Database Static Model

The technology we will be using to implement our database (MongoDB) comes with a library that allows for efficient interfacing through python. Because of this built in advantage, we have designed the system so that the database has one module with which it communicates, the "Database Interpretor." This interface consists of a single type of input and a single type of output. When a user visits the "Popular Palettes" page, the frontend will query that backend which will reach the palette DB as a request to view the collection of palettes. When this query happens, the database will pass the collection on to the database interpretor module in a format that allows for easy movement to the end-users. Below we have included a dynamic model to demonstrate this interface.

.. figure:: images/palette_database_dynamic.png
   :name: palette-database-dynamic
   :scale: 50%

   Palette Database Dynamic Model

The design choices for the palette database module were made with the goal of simplicity. By keeping the number of collections to a minimum and formatting all data entries identically, the organization and movement of Gbiv's data can be straightforward and efficient. This prevents database accessing from being a bottleneck for performance, as well as reduces the need for more modules for data formatting.


Database Interpretor
----------------------







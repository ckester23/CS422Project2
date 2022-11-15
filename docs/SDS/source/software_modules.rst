Software Modules
=================

Frontend Manager
-----------------


Backend Manager
-----------------


Web Interface
---------------


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




Database Interpretor
----------------------







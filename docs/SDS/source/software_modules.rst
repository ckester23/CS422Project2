Software Modules
=================

Below are in depth descriptions of the design of each individual software module. It should be noted that not every component of the software architecture (see :numref:`software-architecture`) is included in this list because not every component is part of the system we implemented. In particular, we do not describe users (for more information on users see the SRS), the Internet, or our web server (for which we used an OOTBS/COTS option).

.. _frontend-manager:

Frontend Manager
-----------------

The purpose of the frontend manager module is to help bind together separate components of the system. In particular, it is one half of the duo that is responsible for bridging the front and the back end (for more information on the other component of that connection see :numref:`backend-manager`). Because the frontend manager acts primarily as a middle ground for passing information and control messages, it does not have much internal structure. However, we can still represent this module in a static fashion using the diagram below:

.. figure:: images/frontend_manager_static.png
   :name: frontend-manager-static
   :scale: 20%

   Frontend Manager Static Model

.. raw:: latex

   \clearpage

The frontend manager acts as a sort of "ambassador" between the frontend and the backend which means it accepts inputs and outputs from both sides. On the backend side, this module gives outputs to the backend manager and receives inputs from the color analyzer. The outputs that are given to the backend manager are control messages that indicate what the user is "asking for," which results in the proper data being generated. The inputs from the backend are different types of data intended to be delivered to end-users. Because this module is implemented using the same framework and technologies as the backend, the data can be transferred directly from where it is generated to the frontend manager. 


In terms of interfacing with the frontend, we can again divide the interactions into inputs and outputs. Inputs from the frontend originate from user interaction which is translated into function calls in the frontend manager. Outputs to the frontend carry information provided by the backend modules, but formatted in a way that works with web display. A dynamic diagram can be used to show these interfaces in a more streamlined way:

.. figure:: images/frontend_manager_dynamic.png
   :name: frontend-manager-dynamic
   :scale: 25%

   Frontend Manager Dynamic Model

.. raw:: latex

   \clearpage

The design rationale behind the frontend manager prioritizes system communication and cohesion. We could have designed Gbiv so that frontend components interfaced directly with backend modules, but by establishing a central place for inputs from and outputs to user-facing modules, we simplified our implementation significantly.  


Web Interface
---------------

The Web Interface module is essential to the system because it defines the user experience in our application. The design of our website follows the traditional multi-page model seen on many popular websites with a navbar at the top to switch between the pages. Each page has a different functionality and displays different information to the user. The general layout of each page is shown visually in the static diagram below:


.. figure:: images/website_static.png
   :name: website-static
   :scale: 50%

   Web Interface Static Model


There are two main interactions that the web interface has with other components in the system. First, it interacts extensively with the users through Internet by way of the server it is hosted on. The web interface is how the user requests the services that Gbiv provides and receives the information that is generated in response to these requests. Because Gbiv is web hosted, the web interface needs the pythonanywhere server in order to properly interface with users.


The second interaction that is key to keep the web interface functioning is the communication between each page and the Frontend Manager module. The Frontend Manager connects the user-facing display with the backend functionality and allows for dynamic pages that respond to user input. These two types of interaction are elaborated on in the dynamic model below:

.. figure:: images/website_dynamic.png
   :name: website-dynamic
   :scale: 30%

   Web Interface Dynamic Model

.. raw:: latex

   \clearpage

The website was designed in this way for two primary reasons: (1) the multi-page website is familiar and therefore easily navigable for our users and (2) having separate pages increases modularity. The former point is important for Gbiv because our target users are a very wide demographic, so we want an intuitive and accessible user interface. The latter point has key advantages when it comes to the development of the system. In particular, modularity allows for easier delegation of tasks and for more efficient and focused debugging when problems arise.

The web interface module can be divided into sub-modules based on separate pages on the site. Below we have a brief description of each page's functionality and structure.

Main Page (Upload an Image)
#############################

This is the page where users can upload an image to have its dominant color extracted and related colors and palettes generated for that dominant color. For more information on the dynamics of this use case see :numref:`use-case-1`. At first the page will only have a skeleton with blank palettes and color blocks, but after the user uploads a valid image, those blocks will be populated with the generated colors and the user's uploaded image will be displayed.


Example Palettes Page
#######################

This page of our website shows a variety of example palettes so that users can get ideas and inspiration for their own color palettes. 


Color Theory Page
##################

This part of the website is purely informational. It will provide users with basic knowledge of color theory and show how the principles of this discipline have been applied in Gbiv to generate new colors after an image has been uploaded.


About Us Page
################

Like the color theory page, the "About Us" page has little to do with the dynamics of Gbiv, rather it exists to provide background to the users. Information about the project and the team are important because it gives users an avenue for contacting the team to report bugs or to become a contributor themselves if we make this system open source in the future.


.. _backend-manager:

Backend Manager
-----------------

The functionality of the backend manager is very similar to that of the frontend manager (see :numref:`frontend-manager`) in that it is middle ground for communication throughout the system. It is a vital part of the overall framework of Gbiv because without it the connection between the front and backend would be much more complex and vulnerable to bugs. Like the other "manager" module, this component is mostly defined by its interaction with other modules. However, we can still make a basic static diagram that shows the structure through which information flows:

.. figure:: images/backend_manager_static.png
   :name: backend-manager-static
   :scale: 20%

   Backend Manager Static Model

.. raw:: latex

   \clearpage


The backend manager has both inputs and outputs from the front and backend. On the frontend, the inputs come in the form of requests for data and/or computation that requires backend modules. The outputs to the frontend are entirely control messages because the backend modules that manage computation and data retrieval can return directly to the frontend manager.

Outputs to the backend come in the form of function calls to either the color analyzer or database interpretor modules. In addition to these function calls, control messages may be passed along to the backend for special cases such as error handling and application updates. To show all of these inputs and outputs in a concise manner we can build a dynamic model for the backend manager:

.. figure:: images/backend_manager_dynamic.png
   :name: backend-manager-dynamic
   :scale: 30%

   Backend Manager Dynamic Model


.. raw:: latex

   \clearpage

This module was designed with ease of communication as the main goal. By establishing a central module where communication from the frontend to the backend passes, we are able to reduce the structural complexity of the system and do more with less function calls. Furthermore, by having the color analyzer return directly to the frontend, we avoided the need for extensive data processing and reformatting.


Color Analysis
-------------------

The primary function of this module is to the color analysis and generation that happens after a user has uploaded a photo. This module is made up of several sub-modules (divided by functionality) which are further divided into sub-sub modules. The static model below gives a visual picture of how the color analysis module is structured.


.. figure:: images/color_analyzer_static.png
   :name: color-analyzer-static
   :scale: 30%

   Color Analysis Module Static Model


As the above model shows, all of the work with color manipulation and analysis is done within the module. This makes for a high level of cohesion that allows for a weak coupling with other modules in the system. In fact, the color analysis module only has to take inputs from a single module which is the "Backend Manager." The backend manager passes an image in the form of a .png, .jpg, or .jpeg file and this module returns several sets of color codes as lists of hex code strings. All outputs of the color analyzer go directly to the frontend manager. The inter-module interactions of this part of the system are further specified in the dynamic model below.


.. figure:: images/color_analyzer_dynamic.png
   :name: color-analyzer-dynamic
   :scale: 25%

   Color Analysis Module Dynamic Model


.. raw:: latex

   \clearpage

This module was designed with a high degree modularity in mind. By separating the color analysis process into two parts, we are able to define two classes of sub-functions that share common features: palette generator functions and related color finder functions. This allows for code re-use and also source code that is easier to read and interpret. We also designed this module to have simple data types as both inputs and outputs. This allows easier integration with the rest of the system and fits well into our chosen framework (Flask).





System Overview
=================

Gbiv is a web application with the goal of making color theory more accessible to the world and inspiring the designer in all of us. Its primary use case is that users can upload images and Gbiv will extract the dominant color and use it to suggest related colors and palettes. In addition to this, Gbiv shows users popular palettes that have been viewed often on the site.

Like most web applications, our system is divided into frontend and backend. On the frontend we have a "frontend manager" module which employs the Flask framework and python code to build the general structure for our user-facing website. The site itself utilizes HTML, CSS, and Bootstrap for styling and extra functionality in terms of user interface. We use the common page system and employ 4 pages: a main page for users to upload images, a page to see popular palettes, an informative page about color theory, and an about page describing the project.

On the backend we have a similar "manager" module which also uses Flask and ties together the front end framework with scripts and a database in the backend. The scripts that contain functions that are called by Flask are divided into two python files: the color analyzer and the database interpretor. The former handles all the color extraction and related color calculation while the latter provides an interface with the database that stores popular palettes. The database is implemented using MongoDB and is accessed using Mongo's provided python library. 

These two sections of the system are tied together using the Flask framework as described above. Gbiv is hosted online using Firebase and the source code is maintained through GitHub provided version control. For more information there are several documents describing Gbiv: the SRS, the SDS (this document), the user documentation, and the developer's manual.
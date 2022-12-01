System Overview
=================

Gbiv is a web application with the goal of making color theory more accessible to the world and inspiring the designer in all of us. Its primary use case is that users can upload images and Gbiv will extract the dominant color and use it to suggest related colors and palettes. In addition to this, Gbiv shows users example palettes for design inspiration.

Like most web applications, our system is divided into frontend and backend. On the frontend we have a "frontend manager" module which employs the Flask framework and python code to build the general structure for our user-facing website. The site itself utilizes HTML, CSS, and Jinja for styling and extra functionality in terms of user interface. We use the common page system and employ 4 pages: a main page for users to upload images, a page to see example palettes, an informative page about color theory, and an about page describing the project.

On the backend we have a similar "manager" module which also uses Flask and ties together the front end framework with scripts and a database in the backend. Beyond the manager we have the color analyzer script (also written in python) which handles all the color extraction and related color calculation.


These two sections of the system are tied together using the Flask framework as described above. Gbiv is hosted online using pythonanywhere and the source code is maintained through GitHub's version control system. Documentation for Gbiv was created using reStructuredText, Sphinx documentation generator, and MS Visio. For team management, we used Jira with Google Drive supporting shared project plan documents. For more information there are several documents describing Gbiv: the SRS, the SDS (this document), the user documentation, and the developer's manual.
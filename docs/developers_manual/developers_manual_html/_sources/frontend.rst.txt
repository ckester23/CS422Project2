Frontend Development Guide
=============================

Overview
----------
This section describes how a developer would go about contributing to the frontend side of Gbiv. This includes the web interface (both static and dynamic pages) as well as the UI/UX as a whole.

Getting Started
-----------------------


Necessary Software
###################

When developing frontend software for Gbiv, it is often helpful to be able to host the website locally to see how changes in the source code affect the application visually. In order to do this, one must download the libraries and packages listed in the requirements.txt file in the root directory. These can be downloaded in your personal system or by setting up a python virtual environment as described in this `link <https://docs.python.org/3/library/venv.html#module-venv>`_. In either your machine or the virtual environment, run the command ``python3 -m pip install -r requirements.txt`` in the command line of your system. Note that depending on the OS you are using and certain configuration settings, this command may vary slightly.


Proficiencies
#################

If a developer wishes to contribute to the styling, specifically of the static pages, basic knowledge of HTML and CSS should suffice for programming experience. However, to add on to the dynamic functionality of Gbiv's frontend, one should familiarize themselves with HTML/CSS as well as Python and Jinja. Python is how inputs and outputs are routed to and from the frontend side, while Jinja is used to generate dynamic page builds based on these interfaces.

Possible Areas of Improvement
------------------------------

- Smoother styling for suggested palettes and related colors
- Implementing a user interface that adapts to user uploaded photos (e.g. incorporating the extracted color in the design)
- More visual explanation on the color theory page


Best Practices
---------------

To begin with, all code should be written according to the accepted style guide for the language being used. Comments should be frequent enough to explain what is going on, but not so common as to complicate the reading of source code. 

When it comes to Gbiv's frontend specifically, Jinja should be used for dynamic web page building, but used sparingly (i.e., only when needed for interaction with the backend). As much as possible, CSS code should be kept to the styles.css file and HTML code should be separated into files based on the page that the code is building on. For Python source files, docstrings should be included for each function and user-defined object. In addition to docstrings inline comments should be used as needed.


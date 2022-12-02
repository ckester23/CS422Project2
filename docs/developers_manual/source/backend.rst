Backend Development Guide
=============================

Overview
----------

This section is to aid developers who wish to contribute to Gbiv on the backend side of things. This applies to backend modules that define Gbiv's framework and routing, as well as the color analyzer module which provides the primary logic behind Gbiv's functionality.


Getting Started
-----------------------

Necessary Software
###################

The software necessary to develop on the backend is very similar to what is needed for frontend developers. Downloading all the requirements listed in the requirements.txt file in the root directory will cover your bases for machine compatibility. If you would like to set up a python virtual environment to do testing, visit this `link <https://docs.python.org/3/library/venv.html#module-venv>`_. Then, either on your local computer or in the virtual environment, run ``python3 -m pip install -r requirements.txt`` (exact syntax may vary based on OS in use). 


Proficiencies
#################

To contribute to or modify the backend codebase a developer should be well versed in python and have at least a basic understanding of the Flask framework. 


Possible Areas of Improvement
------------------------------

- More palettes provided
- Add related colors section in recommender system
- Add filter tags for sample palettes and generated recommendations.


Best Practices
---------------

Developers should adhere to Python style guidelines as well as maintain adequate version control of altered elements to ensure that the codebase remains functional. It is also important to thoroughly comment any added code and to include docstrings/some other type of description for new objects and/or functions.
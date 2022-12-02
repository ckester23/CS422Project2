Documentation Development Guide
=================================

Overview
----------

This section is intended to aid those who wish to contribute to Gbiv's documentation. The documentation for this project can be found in the "docs" folder in the root directory and includes user documentation, an SRS, an SDS, a initial project proposal, and a developer's manual (this document).


What You Need to Start
-----------------------

Software Necessary
###################

To generate builds in the documentation folders, you must have Sphinx downloaded and the Read-The-Docs theme if you wish to create html versions. For more information check out these links to documentation for `Sphinx <https://www.sphinx-doc.org/en/master/>`_ and `Read The Docs <https://sphinx-rtd-theme.readthedocs.io/en/stable/>`_ . In order to create graphics that fit with the style of diagrams used in the documentation, one should use Microsoft Visio (available for purchase `here <https://www.microsoft.com/en-us/microsoft-365/visio/flowchart-software>`_). 

Proficiencies
#################

To add to the documentation a developer should be proficient in reStructuredText for modifying content, Sphinx for generating builds, and Python for configuring Sphinx. Furthermore, contributors to documentation should be familiar with the basics of technical writing--key to this is knowing your audience and adapting the writing style to fit who will be reading the content.


Possible Areas of Improvement
------------------------------

- Further discussion on the specific principles of color theory utilized in the color recommendation script
- More explicit documentation for the source code itself (for development purposes)
- A more in depth explanation of how libraries were used in the system


Best Practices
---------------

Developers should follow standards of reStructuredText as a style guide. They should keep section formatting consistent with existing docs. It is also important to test builds with Sphinx often and to not push anything that has Sphinx errors or warnings. Diagrams included in the documentation should be high resolution and with clear labels and explanations.
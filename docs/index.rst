.. python_voc_parser documentation master file, created by
   sphinx-quickstart on Mon Apr 10 22:09:26 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to python_voc_parser's documentation!
=============================================

An easy way to read pascal voc dataset. For now it only has functionality for the detection competition.

The idea is to have a simple way to get a dataframe from the pascal voc dataset.

Right now the package only has functionality for the detection competition. Pull request are welcome `project on GitHub`_.

.. _`project on GitHub`: https://github.com/gabrielrezzonico/python_voc_parser

Installation
------------

Install from PyPi

.. code-block:: bash

    pip install python_voc_parser


Optionally, install from source:

.. code-block:: bash

    git clone https://github.com/gabrielrezzonico/python_voc_parser.git
    cd python_voc_parser
    pip install .


Usage
-----

Extract the dataset, in this example the dataset was extrated in a folder called "VOCdevkit":

Create a few constants with the paths to the folders

.. code-block:: python

    WORKING_DIRECTORY = os.getcwd()
    # we are going to use all the train and validation images from all categories (trainval.txt)
    IMAGE_SET_PATH = os.path.join(WORKING_DIRECTORY, 'VOCdevkit/VOC2012/ImageSets', 'Main')
    DETECTION_COMPETITION_FILENAME = 'trainval.txt'
    ALL_IMG_DETECTION_COMPETITION_FILEPATH = os.path.join(IMAGE_SET_PATH, DETECTION_COMPETITION_FILENAME)
    # path to the voc annotation folder
    ANNOTATIONS_PATH = os.path.join(WORKING_DIRECTORY, 'VOCdevkit/VOC2012/Annotations')

Create a parser object

.. code-block:: python

    #import the module
    import python_voc_parser as voc 
    #create a parser object
    parser = voc.VocAnnotationParser()

Parse the imageset file and the the folder with all the xml with annotations

.. code-block:: python

    #parse the voc data
    parser.parse_from_voc(ALL_IMG_DETECTION_COMPETITION_FILEPATH, ANNOTATIONS_PATH)
    # if you need a list with all the data:
    annon_list = parser.annotation_line_list
    # if you need a dataframe:
    annon_df = parser.get_annotation_dataframe()


Source code
-----------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   code


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

# python voc parser

An easy way to read pascal voc dataset. For now it only has functionality for the detection competition.

## Installation

Install from PyPi
```bash
pip install python_voc_parser
```

Install from source:

```bash
git clone https://github.com/gabrielrezzonico/python_voc_parser.git
cd python_voc_parser
pip install .
```

## Example usage

Extract the dataset, in this example the dataset was extrated in a folder called "VOCdevkit":

```python
WORKING_DIRECTORY = os.getcwd()
# we are going to use all the train and validation images from all categories (trainval.txt)
IMAGE_SET_PATH = os.path.join(WORKING_DIRECTORY, 'VOCdevkit/VOC2012/ImageSets', 'Main')
DETECTION_COMPETITION_FILENAME = 'trainval.txt'
ALL_IMG_DETECTION_COMPETITION_FILEPATH = os.path.join(IMAGE_SET_PATH, DETECTION_COMPETITION_FILENAME)
# path to the voc annotation folder
ANNOTATIONS_PATH = os.path.join(WORKING_DIRECTORY, 'VOCdevkit/VOC2012/Annotations')
# Image path
IMAGE_PATH = os.path.join(WORKING_DIRECTORY, 'VOCdevkit/VOC2012/JPEGImages')
```

```python
#import the module
import python_voc_parser as voc 
#create a parser object
parser = voc.VocAnnotationsParser(IMAGE_PATH, IMAGE_SET_PATH, ANNOTATIONS_PATH)
```

```python
# if you need a list with all the data:
annon_list = parser.annotation_line_list
# if you need a dataframe:
parser.get_annotation_dataframe()
```

returns:

|   | class_name  | height  | img  | img_full_path  | width  | xmax  | xmin  | ymax  | ymin  |
|---|---|---|---|---|---|---|---|---|---|
| 0  | tvmonitor  | 375.0  | 2008_000002  | /home/user/Personal/playground/voc/VOCdevkit/V...  | 500.0  | 448   | 34 | 293  | 11  |
| 1  | train  | 333.0  | 2008_000003  | /home/user/Personal/playground/voc/VOCdevkit/V...  | 500.0  | 500  | 46  | 333  | 11  |
| 2  | person  | 333.0  | 2008_000003  | /home/user/Personal/playground/voc/VOCdevkit/V...  | 500.0  | 83  | 62  | 243  | 190  |

```python
parser.get_annotation_dataframe_compact()
```

returns:

|   | img_full_path  | annon  |
|---|---|---|
| 0  | /home/user/Personal/playground/voc/VOCdevkit/V...2008_000002.jpg  | (((34, 11, 448, 293), tvmonitor),)  |
| 1  | /home/user/Personal/playground/voc/VOCdevkit/V...2008_000003.jpg  | (((46, 11, 500, 333), train), ((62, 190, 83, 2...  |


## Contribute (Development of the package)

To develop a module based on this project follow this instructions.

### Create a virtualenv for development packages

It's allways a good idea to create an enviroment for the module.

```bash
conda create --name packages_p3 python=3.5
source activate packages_p3
conda install virtualenv
virtualenv venv
```

### Installing dev and test dependencies
```bash
pip install -e .[dev,test]
```

### ​Working in “Development Mode”

While you are developing the module you can install your module from source:

```bash
pip install -e .
```

## Test and coverage

To run the test:

```bash
$ py.test tests
==================================== test session starts =====================================
...
collected 4 items

tests/test_hello.py ...s

============================ 3 passed, 1 skipped in 0.02 seconds =============================
```

To run the coverage:

```bash
$ py.test --cov=python_package tests/

 ==================================== test session starts =====================================
 ...
tests/test_hello.py ...s
----------- coverage: platform linux, python 3.5.3-final-0 -----------
Name                         Stmts   Miss  Cover
------------------------------------------------
python_package/__init__.py       1      0   100%
python_package/example.py        5      0   100%
------------------------------------------------
TOTAL                            6      0   100%

============================ 3 passed, 1 skipped in 0.05 seconds =============================
```

## Convert README.md to README.rst

```bash
pandoc --columns=100 --output=README.rst --to rst README.md
```
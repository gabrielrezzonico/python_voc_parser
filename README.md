# Minimal package/module sample

Minimal python module/package sample project. Only defines a class with dummy functionality and some demo tests. Minimal project structure.

## TODO

* generate documentation using Sphinx
* create account at pypi.python.org and add .pypirc file
* git tag and release on github
* publish the package

## Project structure

| File or folder  | Description  |
|---|---|
| setup.py  | Module configuration.  |
| setup.cfg  | PyPi configuration.  |
| README.md  | this file.  |
| python_package/  | The actual package/module. Where all the code resides.  |
| tests/  | Sample unit test using py.test.  |


## Development

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
python3 
```

And you can import the module and testing in python.

```bash
$ ▶ python3
Python 3.5.3 |Continuum Analytics, Inc.| (default, Mar  6 2017, 11:58:13)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import python_package
>>> type(ob)
<class 'python_package.example.Example'>
>>> ob.hello()
'Hello!!'
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

## Generate documention

To generate documentation:

```bash
cd docs
make html
```

The index.html is generated based on docs/index.rst. A simple file of how to autogenerate documentation from the docstring on your code can be found in docs/code.rst, this use autocode. for more infomation you can read:

* [Sphinx](http://www.sphinx-doc.org/en/stable/tutorial.html) 

* [Autodoc](http://www.sphinx-doc.org/en/stable/ext/autodoc.html)
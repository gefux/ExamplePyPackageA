# ExamplePyPackageA
Example setup of a Python 3 package

[![Build Status](https://travis-ci.com/gefux/ExamplePyPackageA.svg?branch=main)](https://travis-ci.com/gefux/ExamplePyPackageA)

## Steps:

### 1. Create repo on Github

* Pick a .gitignore file
* Important: **choose a license**!
* Create a README.md

### 2. Add the package code

* Make sure the `__init__.py` file facilitates not more and not less than what
  you think your API should facilitate.

### 3. Add version

* Add a file that states the version of the package.

### 4. Make package installable for pip

* Create a `setup.py` file
* Create a `requirements.txt` file (to capture on what other packages your
  package depends on)

Now you should be able to install the package by navigating to the packages and
executing:
```
python3 -m pip install .
```

### 5. Create test environment

* Create `requirements_ci.txt` with all dependencies needed for the contineous
  integration. This includes the normal requrements plus any other packages
  needed for testing or creating the documentation later.
* Create `tox.ini` to create a tox environment for testing.
* Create a test.

### 6. Connect travis-ci for automated testing

* Log into travis-ci.com with github account and allow travis to access your
  github.
* Add the repo to travis.
* Add travis configuration in `.travis.yml`
* From now on travis will run the test after every push to github.
* Add the build-badge (just to show off) on the top on the readme. You can get
  it by clicking on the build-badge icon on the build of the repo on travis.
  It is a link and changes depending on the outcome of the last build.

### 7. If not already in place: DOCUMENTATION!

* There should be at least complete docstrings. I recommend using some standard like the numpydoc docstring:
  <https://numpydoc.readthedocs.io/en/latest/format.html>
* Using such a consistant docstring standard as the advantage that you can use [`sphinx`](https://www.sphinx-doc.org) to automatically generate a nice documentation webpage and display it with https://readthedocs.org/ (linking it to the github repo).
* Also, you might want to have a simple quickstart example in your README.md

------------------------------------------------------------------------------

## Quickstart (example)

Make sure you have Python3.6 or higher installed.
Install the package with pip like this:
```
$ python3 -m pip install example_py_package_a
```

Run `python3` and try to do some exciting divisions!
``` python
$ python3
Python 3.6.9 (default, Oct  8 2020, 12:12:24)
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import example_py_package_a as eppa
>>> eppa.a_divided_by_b(-7,2)
(-4, 1)
>>> eppa.a_divided_by_b(14,0)
(42, 14)
>>> exit()
```

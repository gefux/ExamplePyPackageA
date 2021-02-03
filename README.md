# ExamplePyPackageA
Example setup of a Python 3 package

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

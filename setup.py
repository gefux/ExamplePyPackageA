# Copyright (c) 2021 Gerald E. Fux
#
# Licensed under the MIT License

import os
import sys

from setuptools import find_packages
from setuptools import setup
import pkg_resources

here = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, here)

# get the __version__ variable
with open(os.path.join(here,"example_py_package_a/version.py"), "r") as f:
  exec(f.read(), globals())

# get short and long description
short_description = \
"An example Python 3 package (A)."

with open(os.path.join(here,"README.md"), "r") as f:
  long_description = f.read()

# get requirements list
with open(os.path.join(here,"requirements.txt"), "r") as requirements_file:
    requirements = requirements_file.readlines()

setup(
    name='example_py_package_a',
    version=__version__,
    url='https://github.com/gefux/ExamplePyPackageA',
    author='Gerald E. Fux',
    author_email='gerald.e.fux@gmail.com',
    python_requires=('>=3.6.0'),
    install_requires=requirements,
    license='MIT',
    description=short_description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords = ['pure-mathematics',
                ],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent",
    ]
)

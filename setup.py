import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "py_localize",
    version = "0.2",
    author = "Bertrand Tornil",
    author_email = "bertrand.tornil@gmail.com",
    description = ("Useless HTTP localization service based on Maxmind GeoIP "),
    license = "MIT",
    keywords = "Localization Maxmind Bottle Training",
    url = "",
    packages = ['localize'],
    scripts = ['localize/app.py'],
    test_suite = 'tests',
    long_description = read('README.md'),
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)


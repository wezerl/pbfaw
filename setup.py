"""praw setup.py"""

import re
from codecs import open
from os import path

from setuptools import find_packages, setup

PACKAGE_NAME = "pbfaw"
HERE = path.abspath(path.dirname(__file__))
with open(path.join(HERE, "README.rst"), encoding="utf-8") as fp:
    README = fp.read()
with open(path.join(HERE, PACKAGE_NAME, "const.py"), encoding="utf-8") as fp:
    VERSION = re.search('__version__ = "([^"]+)"', fp.read()).group(1)

extras = {
    "ci": ["coveralls"],
    "dev": ["packaging"],
    "lint": ["pre-commit"],
    "readthedocs": ["sphinx", "sphinx-rtd-dark-mode", "sphinx_rtd_theme"],
    "test": [
        "betamax >=0.8, <0.9",
        "betamax-matchers >=0.3.0, <0.5",
        "pytest >=2.7.3",
        "requests >=2.20.1, <3",
    ],
}
extras["lint"] += extras["readthedocs"]
extras["dev"] += extras["lint"] + extras["test"]

setup(
    name=PACKAGE_NAME,
    author="Wezerl",
    author_email="Wezerlsstuff@gmail.com",
    python_requires="~=3.7",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Utilities",
    ],
    description=(
        'PRAW, an acronym for "Python Reddit API Wrapper", is a python package that'
        " allows for simple access to  Reddit's API."
    ),
    extras_require=extras,
    install_requires=[
        "prawcore >=2.1, <3",
        "update_checker >=0.18",
        "websocket-client >=0.54.0",
    ],
    keywords="reddit api wrapper",
    license="Simplified BSD License",
    long_description=README,
    package_data={"": ["LICENSE.txt"], PACKAGE_NAME: ["*.ini", "images/*.png"]},
    packages=find_packages(exclude=["tests", "tests.*", "tools", "tools.*"]),
    project_urls={
        "Issue Tracker": "https://github.com/wezerl/praw/issues",
        "Source Code": "https://github.com/wezerl/praw",
    },
    version=VERSION,
)

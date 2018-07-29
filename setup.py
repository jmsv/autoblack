#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import re
from codecs import open
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(path.join(here, "autoblack/__init__.py"), encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="autoblack",
    version=version,
    description="watch python files for changes and format them using black",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jmsv/autoblack",
    author="James Vickery",
    author_email="dev@jamesvickery.net",
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["autoblack"],
    python_requires=">=3.4, <4",
    keywords="autoblack black automation formatter yapf autopep8 pyfmt gofmt rustfmt",
    install_requires=["black"],
    entry_points={"console_scripts": ["autoblack=autoblack:main"]},
    project_urls={
        "Source": "https://github.com/jmsv/autoblack",
        "Bug Reports": "https://github.com/jmsv/autoblack/issues",
    },
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name="Livej Spider",
    version="0.1",
    packages=find_packages(),
    #    package_dir = {'': 'livej'},
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['Pillow'],
    py_modules=['items', 'pipelines', 'settings'],
    entry_points={'scrapy': ['settings = livej.settings']},
    # metadata for upload to PyPI
    #    author = "Andrey",
    author_email="knevcher@gmail.com",
    description="This is an Example Package",
    license="PSF",
    keywords="hello world example examples",
    zip_safe=True,
    include_package_data=True,
)

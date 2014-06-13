#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

__author__ = "Brandon Wood"
__copyright__ = "Copyright 2014, Brandon Wood"
__license__ = "BSD"

__version__ = "0.0.4"
__maintainer__ = "Brandon Wood"
__email__ = "btwood+rural@geometeor.com"
__status__ = "Development"

setup(name='rural',
      version=__version__,
      description='Simple command line utility for uploading files to AWS S3, \
      copying a public link to that file to the clipboard',
      author=__author__,
      author_email=__email__,
      license=__license__,
      url='https://github.com/woodb/rural',
      packages=find_packages(),
      scripts=['rural'],
      install_requires=['boto', 'click', 'xerox'],
    )

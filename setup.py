#!/usr/bin/env python
# -*- coding: utf8 -*-

from setuptools import setup

setup(name='imhdsk',
      version='0.0.5',
      description='An unofficial API for imhd.sk',
      maintainer='mr.Shu',
      maintainer_email='mr@shu.io',
      url='https://github.com/mrshu/python-imhdsk-api',
      packages=['imhdsk'],
      install_requires=['requests', 'lxml'])

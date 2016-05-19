#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

dependencies = [
  'docopt',
  'gitpython',
  'pypng'
]

setup(
  name='genlog',
  version='0.0.1',
  description='genlog',
  url='',
  license='MIT License',
  author='Anders Hoff',
  author_email='inconvergent@gmail.com',
  install_requires=dependencies,
  packages=[
    'genlog'
  ],
  entry_points={
    'console_scripts': [
      'genlog=genlog:run'
    ]
  },
  zip_safe=True
)


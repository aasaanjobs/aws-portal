#!/usr/bin/env python

from setuptools import setup

setup(name='aws-portal',
  version='0.1',
  author='Shubham Bhartiya',
  author_email='bhartiya.shubham08@gmail.com',
  scripts=['aws-portal'],
  install_requires=['boto', 'simplejson'],
)

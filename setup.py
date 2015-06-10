#!/usr/bin/env python

from setuptools import setup

setup(name='aws-portal-setup',
  version='1.0',
  author='Shubham Bhartiya',
  author_email='bhartiya.shubham08@gmail.com',
  scripts=['aws-portal'],
  install_requires=['boto', 'simplejson'],
)
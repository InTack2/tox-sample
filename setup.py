# !/usr/bin/env python
from setuptools import setup
from setuptools import find_packages

install_requires = [
    "requests",
]


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(name='tox_sample',
      version='0.1',
      description='tox_sample',
      author='tox_sample',
      author_email='sample@sample.sample',
      url='',
      packages=find_packages("src.tox_sample"),
      install_requires=install_requires
      )

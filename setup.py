# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='clean-architecture',
    version='0.1.0',
    description='Clean Architecture - Python',
    long_description=readme,
    author='Enilton Angelim',
    author_email='enilton.angelim@gmail.com',
    url='https://github.com/eniltonangelim/clean-architecture',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
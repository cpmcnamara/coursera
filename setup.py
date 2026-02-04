#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='coursera',
    version='0.1.0',
    description='Coursera API client library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Coursera',
    url='https://github.com/cpmcnamara/coursera',
    packages=find_packages(exclude=['tests', 'docs', 'book']),
    install_requires=requirements,
    python_requires='>=2.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
)

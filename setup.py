#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 11:55:45 2023

@author: tripatpanesar
"""

# setup

from setuptools import setup, find_packages

setup(
    name='booklover',
    version='1.0.0',
    url='https://github.com/tripatpanesar/booklover.git',
    author='Tripat Panesar',
    author_email='tp6mt@virginia.edu',
    description='For HW 9',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)

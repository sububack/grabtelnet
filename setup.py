#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

VERSION = '1.1.0'

setup(
    name='grabtelnet',
    version=VERSION,
    scripts=['grabtelnet',],
    author='Subramanian K',
    author_email='sububack@gmail.com',

    maintainer='Subramanian K',
    maintainer_email='sububack@gmail.com',

    description='telnet console dump and timing program',
    long_description='''
grabtelnet is a small program similar to grabserial which reads a terminal console
port and writes data to standard output. The main purpose of this tool to
collect messages written to the terminal console from a target system and save
the messages on a host machine.
''',
    url='http://github.com/sububack/grabtelnet',
    license='GPL v2',
    keywords='grabtelnet boot time optimization tool',
    classifiers=[
        "Topic :: Utilities",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.0",
        "Topic :: Software Development :: Embedded Systems",
    ],
)

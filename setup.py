#!/usr/bin/env python
#
"""
@author: Adam Kniffen <adam_kniffen@trendmicro.com>
@organization: Serapis
@updated: 04SEP2018
"""

from setuptools import setup

setup(
    name='martinsMajesticMenagerie',
    version='0.1',
    packages=['app', 'app.core'],
    entry_points={
        'console_scripts': [
            'got=app.core.__main__:main'
        ]
    },
    url='https://github.com/akniffe1/martinsMajesticMenagerie',
    install_requires=['click', 'requests', 'pandas', 'numpy'],
    license='Apache2.0',
    author='knifehands',
    author_email='adamkniffen@gmail.com',
    description=''
)

#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from defectdojo_api import __version__ as version

with open('README.rst', 'r') as f:
    readme = f.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

version = version.split('.')
version[0] = str(int(version[0]) + 1000)
version = '.'.join(version)

setup(
    name='defectdojo_api',
    packages=['defectdojo_api'],
    version=version,
    description='An API wrapper for DefectDojo. - unnofficial',
    long_description=readme,
    author='Aaron Weaver, modified  by Pedro Galindo',
    author_email='aaron.weaver2@gmail.com - pedrogalindomorey@gmail.com',
    url='https://github.com/p3r1c0/defectdojo_api',
    download_url='https://github.com/aaronweaver/defectdojo_api/tarball/' + version,
    license='MIT',
    install_requires=['requests'],
    keywords=['dojo', 'api', 'security', 'software'],
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
)

#!/usr/bin/python

from setuptools import setup
import os

# Utility function to read the README file in the root directory to be used as the long description
# for the module.
def read_long_description(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

'''
Main setup function used for building and configuring the pyserver python module.
'''
setup(
    name = "pyserver",
    version = "0.0.1",
    author = "raz",
    author_email = "n/a",
    description = "Lightweight HTTP python server.",
    packages = ['pyserver'],
    long_description = read_long_description('README'),
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Service"
    ],
    data_files = [
        ('/lib/systemd/system/', ['systemd/pyserver.service']),
        ('/usr/sbin/', ['service_start.py'])
    ]
)



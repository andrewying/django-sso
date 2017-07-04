#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys

from setuptools import setup, find_packages

setup(
    name="django-sso",
    version="0.0.1",
    description="django-sso",
    long_description=open('README.md').read(),
    author='Andrew Ying',
    author_email='andrew@janoticketing.com',
    url="https://github.com/jano-may-ball/django-sso",
    license="GPLv3",
    classifiers=[
        "Framework :: Django",
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2",
        ],
    keywords='oauth2,sso',
    packages=find_packages(),
    include_package_data=True,
    )

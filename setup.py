#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from codecs import open
import urllib.request as urlrequest
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools import setup
import re
import os
import sys

# get version
with open('s2/__init__.py', 'r', 'utf-8') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

# use requirements.txt as deps list
with open('requirements.txt', 'r', 'utf-8') as f:
    required = f.read().splitlines()

# get readme
with open('docs/index.md', 'r', 'utf-8') as f:
    readme = f.read()

test_deps = ["green>=2.5.0", "coverage"]

setup(name='s2',
      packages=["s2"],
      version=version,
      keywords=['Semantic Scholar', 'API'],
      description="Wrapper for the Semantic Scholar API.",
      long_description=readme,
      url='https://github.com/lum-ai/s2',
      #download_url="https://github.com/s2/s2/archive/v{}.zip".format(version),
      author='LUM.AI',
      author_email='ghp@lum.ai',
      install_requires=required,
      # cmdclass={
      #   'install': SHIInstall,
      #   'develop': SHIDevelop,
      # },
      classifiers=(
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python :: 3"
      ),
      tests_require=test_deps,
      extras_require={
        'test': test_deps
      },
      include_package_data=True)
      #zip_safe=False)

# -*- coding: utf-8 -*-
"""
    Copyright (C) 2013 Kouhei Maeda <mkouhei@palmtb.net>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import sys
from setuptools import setup, find_packages

sys.path.insert(0, 'src')
import shiori

classifiers = [
    "Development Status :: 3 - Alpha",
    "License :: OSI Approved :: "
    "GNU General Public License v3 or later (GPLv3+)",
    "Programming Language :: Python",
]

long_description = \
    open(os.path.join("docs", "README.rst")).read() + \
    open(os.path.join("docs", "HISTORY.rst")).read() + \
    open(os.path.join("docs", "TODO.rst")).read()

requires = ['setuptools', 'oauth2']

setup(name='shiori',
      version='0.1',
      description='bookmarking',
      long_description=long_description,
      author='Kouhei Maeda',
      author_email='mkouhei@palmtb.net',
      url='https://github.com/mkouhei/shiori',
      license=' GNU General Public License version 3',
      classifiers=classifiers,
      packages=find_packages('shiori'),
      package_dir={'': 'shiori'},
      data_files=[],
      install_requires=requires,
      include_package_data=True,
      extras_require=dict(test=['pytest', 'pep8'],),
      test_suite='tests.runtest',
      tests_require=['pytest', 'pep8'])

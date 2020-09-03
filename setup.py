# ------------------------------------------------------------------------------
#  GNU General Public License
#
#  Copyright (c) 2020, Hieu Pham.
#
#  This file is part of Py-Architect.
#  <https://github.com/hieupth/pyarchitect>
#
#  Py-Architect is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Py-Architect is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Py-Architect. If not, see <https://www.gnu.org/licenses/>.
# ------------------------------------------------------------------------------
from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pyarchitect',
    packages=find_packages(),
    version='0.0.6.3.2',
    license='GPLv3',
    description='Implementations of common data structures, design patterns and useful utilities',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Hieu Pham',
    author_email='hieupt.ai@gmail.com',
    url='https://github.com/hieupth/pyarchitect',
    download_url='https://github.com/hieupth/pyarchitect/archive/v_01.tar.gz',
    keywords=['data structure', 'design pattern', 'software architect'],
    install_requires=[],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)

#!/usr/bin/env python3

from os import path
from setuptools import setup, find_packages

package = 'migcon'

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name=package,
      version="1.0",
      description='Utilities to migrate Confluence export to Sphinx, Juypter Book, etc.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Daniel Rapp',
      author_email='rappdw@gmail.com',
      url='https://github.com/rappdw/migcon',
      license='Apache2',
      packages=find_packages(exclude=['tests*']),
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Version Control :: Git',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
      ],
      platforms=["Windows", "Linux", "Mac OS-X"],
      install_requires=[
            'anytree>=2.8.0',
            'markdown_it_py>=1.1.0',
            'pyyaml>=6.0',
      ],
      extras_require={
            'dev': [
                  'wheel>=0.29'
            ],
      },
      entry_points = {
            'console_scripts': ['con2jb=migcon.con2jb:main'],
      }
)
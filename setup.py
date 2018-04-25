from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tabletop-schlepper',
    version='0.0.1',
    description='Export Tabletop Simulator scripts to a lua file, and reimport it',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='David Perry',
    author_email='d.perry@utoronto.ca',
    url='https://www.github.com/Boolean263/tabletop-schlepper',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ttschlep=ttschlepper:main',
        ],
    },
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='annots',
    version='0.1.1',
    description="annots is the package that allow to use Python 3.6 variable annotations in handy way.",
    long_description=readme + '\n\n' + history,
    author="Sergey Khalymon",
    author_email='sergiykhalimon@gmail.com',
    url='https://github.com/infernion/annots',
    packages=[
        'annot',
    ],
    package_dir={'annot':
                 'annot'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='annots annotations typing',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)

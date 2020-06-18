#!/usr/bin/env python
import setuptools 

install_requires = [
        "numpy",
        "scipy",
        "ipython",
        "jupyter",
        "mypy",
        "pytest",
        ]

keywords = [
        "i ching",
        "philosophy",
        "randomness",
        "probability",
        ]

setup(name='iChing',
        version='0.1',
        author='Adam McCartney',
        author_email='adam@mur.at',
        install_requires=install_requires,
        keywords=", ".join(keywords),
        name="iChing",
        packages=['iChing'],
        platforms="Any",
        url="https://github.com/adamccartney/iChing"
        )

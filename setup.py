#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open("README.md") as readme_file:
    readme_data = readme_file.read()

signoff_version = '0.2.1'

setup(
    name="arch-signoff",
    version=signoff_version,
    description="Sign off Arch Linux test packages",
    long_description=readme_data,
    author="Håvard Pettersson",
    author_email="mail@haavard.me",
    url="https://github.com/archlinux/arch-signoff",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Topic :: Software Development",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
    ],

    install_requires=[
        "click",
        "python-dateutil",
        "pyalpm",
        "requests"
    ],

    packages=["signoff"],
    entry_points="""
        [console_scripts]
        signoff=signoff:main
    """
)

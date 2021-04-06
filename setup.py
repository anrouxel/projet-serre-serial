#!/usr/bin/env python
import setuptools

setuptools.setup(
    name="projet-serre-serial",
    version="1.0",
    author="anrouxel",
    description="Application de liaison série entre l'ordinateur (Raspberry PI) et l'Arduino",
    install_requires=["pyserial", "requests"],
    scripts=["projet-serre-serial"],
)
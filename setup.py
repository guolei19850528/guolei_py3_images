#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="guolei-py3-images",
    version="2.0.0",
    description="郭磊 Images API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guolei19850528/guolei_py3_images",
    author="guolei",
    author_email="174000902@qq.com",
    license="MIT",
    keywors=["images", "image", "img", "pic", "picture"],
    packages=setuptools.find_packages('./'),
    install_requires=[
        "addict",
        "retrying",
        "jsonschema",
        "imgkit",
        "Pillow",
    ],
    python_requires='>=3.0',
    zip_safe=False
)

#!/usr/bin/env python

"""
setup.py file for SWIG example
"""

from setuptools import setup, Extension


example_module = Extension(name='_example',
                           sources=['example_wrap.cpp', 'example.cpp'],
                           )

setup (name = 'example',
       version = '0.1',
       author      = "SWIG Docs",
       description = """Simple swig example from docs""",
       ext_modules = [example_module],
       py_modules = ["example"],
       )
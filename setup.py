# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 15:10:30 2020

@author: Kamar
"""

import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='quadratic_root',  
     version='0.0.1 ',
     author="Kamorudeen Amuda",
     author_email="akindeleamuda@gmail.com",
     description="Quadratic equation package",
     zip_safe=False,
     long_description="This is package will help you to find the roots of quadratic equation by just providing the values of a,b and c.",
     long_description_content_type="text/markdown",
     package_dir={'':'quadratic'},
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],python_requires='>=3.6',
 )

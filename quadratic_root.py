# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 10:06:56 2020

@author: Kamar
"""
from math import sqrt

def quad(a,b,c):
    root = ((b**2) - (4*a*c))
    if root < 0:
        root=abs(complex(root))
        j=complex(0,1)
        x1=(-b + j + sqrt(root))/(2*a)
        x2= (-b - j +sqrt(root))/(2*a)
        return x1, x2
    else:
        x1=(-b+sqrt(root))/(2*a)
        x2=(-b-sqrt(root))/(2*a)
        return x1, x2

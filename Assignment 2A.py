# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:28:41 2019

@author: HP
Taylor series computation
"""

def evaluateTaylor (x):
    b=x-1
    taylor= b-b**2/2+b**3/3
    return taylor
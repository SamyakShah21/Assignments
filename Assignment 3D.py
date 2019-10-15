# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 23:30:07 2019

@author: HP
"""

import numpy as np
import math
R=6.371e6
g0=9.82
def gravitationalPull(x):
    if x>=R:
        g=g0*(R/x)**2
    else:
        g=g0*x/R
    return g
    
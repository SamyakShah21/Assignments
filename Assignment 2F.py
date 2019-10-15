# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 18:01:22 2019

@author: HP
"""

import math
import numpy as np
def computeProjection(a):
    projection=sum(a)*a/np.dot(a,a) # sum is used here because dot product with b is actually the sum of each element of vector a
    return projection

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 14:41:48 2019

@author: HP
"""

import numpy as np
def computeItemCost(resourceItemMatrix,resourceCost):
    return np.dot(resourceItemMatrix.T,resourceCost)
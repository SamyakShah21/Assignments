# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 23:41:49 2019

@author: HP
"""

import numpy as np
import math
import matplotlib.pyplot as plt
x=np.arange(0,10e6,1e4)
g=np.zeros(np.size(x))
R=6.371e6
g0=9.82
def gravitationalPull(x):
    g[x<R]=g0*x[x<R]/R
    g[x>=R]=g0*(R/x[x>=R])**2
    return g
plt.plot(x,gravitationalPull(x))
plt.show()
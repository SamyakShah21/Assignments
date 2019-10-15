# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 20:49:01 2019

@author: HP
"""


import matplotlib.pyplot as plt
import numpy as np
p=np.arange(0,2*np.pi,0.01)
plt.plot(np.sin(p),np.cos(p))
plt.plot(xvals,yvals,'o')
plt.show()
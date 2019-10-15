# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:53:42 2019

@author: HP
"""

import numpy as np
import matplotlib.pyplot as plt
import math
x=np.random.uniform(-10,10,2000)
y=np.random.uniform(-10,10,2000)
xnow=np.zeros(0,dtype=int)
ynow=xnow
for i in range(2000):
    if max(abs(x[i]),abs(y[i]))>5 and math.sqrt(x[i]**2+y[i]**2)<10:
        xnow=np.append(xnow,x[i])
        ynow=np.append(ynow,y[i])
    
plt.plot(xnow,ynow,"bo")

plt.show()
        
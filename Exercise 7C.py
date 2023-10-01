# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 15:54:00 2019

@author: HP
Plotting histograms
"""

import numpy as np
import matplotlib.pyplot as plt
x=(np.random.rand(500)<0.5 ) +0       #command to convert it to ineger name_of_array.astype(int)
plt.hist(x,2)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
x=np.ceil(6*np.random.rand(500))
plt.hist(x,6)
plt.show

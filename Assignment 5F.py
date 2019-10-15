# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 23:24:12 2019

@author: HP
"""

import numpy as np
def thermoEquilibrium(N,r):
    time=1
    nl=N-1
    nr=1
    i=1   # the first value does not matter actually
    while(nl!=nr):
        if r[i]<nl/N:
            nl=nl-1
            nr=nr+1
        else:
            nl=nl+1
            nr=nr-1
        i=i+1
        time=time+1
        if (i==np.size(r)):
            return 0
    return time
        plt.plot(x,y)
        plt.show()
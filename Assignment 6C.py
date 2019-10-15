# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:55:51 2019

@author: HP
"""

import numpy as np
def movingAvg(y):
    a=np.zeros((5,np.size(y)))
    b=np.array([0,0])
    ydash=np.concatenate((b,y,b))
    k=4
    for i in range(5):
        for j in range(np.size(y)):
            a[i][j]=ydash[j+k]
        k=k-1
    
    a[0,:]=a[0,:]
    a[1,:]=2*a[1,:]
    a[2,:]=3*a[2,:]
    a[3,:]=2*a[3,:]
    a[4,:]=a[4,:]
    
    z=np.zeros(np.size(y))     
    for i in range(np.size(y)):          # instead of np.size you can use len (sth)
        z[i]=np.sum(a,axis=0)[i]/9
    return z
   
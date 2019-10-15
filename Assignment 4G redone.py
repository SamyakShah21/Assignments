# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 18:01:34 2019

@author: HP
"""

import numpy as np
import math
def clusterAnalysis(reflectance):
    a= np.ones(np.size(reflectance))
    for i in range(np.size(reflectance)):
        if i%2==0:
            a[i]=1
        else:
            a[i]=2
    assnew=a.copy()
    assold=np.zeros(np.size(reflectance))
    while not (assnew==assold).all():
        mean_even=np.mean(reflectance[a==2])
        mean_odd=np.mean(reflectance[a==1])
        for j in range(np.size(reflectance)):
            if abs(reflectance[j]-mean_odd)<=abs(reflectance[j]-mean_even):
                a[j]=1
            else:
                a[j]=2
        
        assold=assnew.copy()
        assnew=a.copy()
    return assnew


# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 12:24:49 2019

@author: HP
"""

import math
import numpy as np
def removeIncomplete (id):
    new_array=np.copy(id)
    i=0
    counter=0
    while (i<np.size(new_array)):
        j=0
        k=0
        while (k<np.size(new_array)):
            if round(new_array[i])==round(new_array[k]):
                j=j+1
            k=k+1
        if j<3:
            i1=i-counter
            counter=counter+1
            id=np.delete(id,i1)
        i=i+1
    return id

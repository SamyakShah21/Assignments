# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 19:24:34 2019

@author: HP
"""

import numpy as np
import string as s
alphabet=list(s.ascii_lowercase)
def letterFrequency(filename):
    filein=open(filename,"r")      # opens file for reading
    lines=filein.readlines()       # no necessity to convert to list
    file_as_string=str.lower(" ".join(lines))
    count=np.zeros(26)
    
    for i in range(len(file_as_string)):
        for j in range(26):
            if(file_as_string[i]==alphabet[j]):
                count[j]=count[j]+1
    frequency=count*100/sum(count)
    return frequency
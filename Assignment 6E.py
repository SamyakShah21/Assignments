# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 21:55:30 2019

@author: HP
"""

import numpy as np
import pandas as pd
def computeLanguageError(freq):
    error=np.zeros(15)
    data=pd.read_csv("letter_frequencies.csv")
    for i in range(1,16,1):                                 #start,stop,step
        for j in range(26):
            error[i-1]=error[i-1]+(data.iloc[j][i]-freq[j])**2
    return error 
    
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 21:45:55 2019

@author: HP
"""

import string as s
import numpy as np
def textToNato(plainText):  
     # if data type is written str then the length at max is set at 1 character
                                                    #so we initialize it to max o=value 8 corresponding to november
    alphabet=s.ascii_lowercase                     # this way we avoid truncation (unwanted)
    coded_joined=""
    key=np.array(["Alpha","Bravo","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India","Juliet","Kilo","Lima","Mike","November","Oscar","Papa","Quebec","Romeo","Sierra","Tango","Uniform","Victor","Whiskey","Xray","Yankee","Zulu"])
    for i in range(len(plainText)):
        for j in range(26):
            if str.lower(plainText[i])==alphabet[j]:
                coded[i]=key[j]
                coded_joined=coded_joined+"-"+key[j]
               
        
    return coded_joined[1:]   # first element is '-' so we do not need that
                                # or use str.replace('-','',1)
    
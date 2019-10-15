# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 00:16:28 2019

@author: HP
"""

import math
import numpy as np
def computePassesGoalLine (point, directionVector):
    d=directionVector
    p=point
    slope=d[1]/d[0]
    if d[0]>0:
        m=p[1]+ (105-p[0])*slope
        if m<37.66 and m>30.34:
            return "True"
        else:
            return "False"
    elif d[0]<0:
        m=p[1]+ (-p[0])*slope
        if m<37.66 and m>30.34:
            return "True"
        else:
            return "False"
    else:
        return "False"
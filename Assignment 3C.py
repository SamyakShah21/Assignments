# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 23:21:55 2019

@author: HP
"""

import math
import numpy as np
def acuteAngle(v1,v2):
    angle=math.acos(np.dot(v1,v2))
    if angle<math.pi/2:
        return angle
    else: 
        return math.pi-angle
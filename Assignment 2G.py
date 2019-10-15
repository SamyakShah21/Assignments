# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 18:10:18 2019

@author: HP
"""

import math
import numpy as np
def boxArea (Corners,area):
    if area == "Box1":
        a=(Corners[1]-Corners[0])*(Corners[5]-Corners[4])
    elif area =="Box2":
        a=(Corners[3]-Corners[2])*(Corners[7]-Corners[6])
    elif area =="Intersection":
        a=max(0,(min(Corners[1],Corners[3])-max(Corners[0],Corners[2])))*max(0,(min(Corners[5],Corners[7])-max(Corners[4],Corners[6])))
    elif area =="Union":
        a=(Corners[1]-Corners[0])*(Corners[5]-Corners[4])+(Corners[3]-Corners[2])*(Corners[7]-Corners[6])- max(0,(min(Corners[1],Corners[3])-max(Corners[0],Corners[2])))*max(0,(min(Corners[5],Corners[7])-max(Corners[4],Corners[6])))
    return a
    
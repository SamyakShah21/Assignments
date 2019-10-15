import numpy as np
import math
def circleAreaMC(xvals,yvals):
    n=0
    for i in range(np.size(xvals)):
        if math.sqrt(xvals[i]**2+yvals[i]**2)<1:
            n=n+1
    area=4*n/np.size(xvals)
    return area
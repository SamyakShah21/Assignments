import math
import numpy as np
def removeIncomplete(id):
    i=0
    a=np.array([])
    while(i<np.size(id)):
        m=0
        k=0
        while(m<np.size(id)):
            if round(id[i])==round(id[m]):
                k=k+1
            if k==3:
                a=np.concatenate((a,np.array([id[i]]))
                
            m = m+1
        i=i+1
    return a
import numpy as np
import math
def clusterAnalysis(reflectance):
    
    a=np.ones(np.size(reflectance))
    for i in range(np.size(reflectance)):
        if i%2==0:
            a[i]=1
        else:
            a[i]=2

    
    assnew=a
    j=0
    while j==0 or assold.all()!=assnew.all():
         assold=assnew
         meanodd=sum(reflectance[a==1])/np.sum(a==1)
         meaneven=sum(reflectance[a==2])/np.sum(a==2)
         for k in range(np.size(reflectance)):
             if abs(a[k]-meaneven)<abs(a[k]-meanodd):
                 a[k]=2
             else:
                 a[k]=1
         
         assnew=a
         j=j+1
    
    return assnew
            
            
          
    
# using vectorized computations for better
# Computes the rate of fermentation
import math
import numpy as np
def fermentationRate(measuredRate, lowerBound, upperBound):
    measuredRate[(measuredRate>=upperBound)] =0 
    measuredRate[ measuredRate<=lowerBound]=0
    new_len=np.size(measuredRate[measuredRate!=0])
    mean= sum(measuredRate)/new_len
    return mean
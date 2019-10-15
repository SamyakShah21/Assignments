# assignment of i should be done inside the function not outside
# take care of position of if statement to satisfy base case 
def bacteriaGrowth(n0,alpha,K,N):
    i=0
    while (True):
        if n0>=N:
            break
        n0=(1+alpha*(1-(n0/K)))*n0
        i=i+1
       
    return i
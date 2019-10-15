import numpy as np
import matplotlib.pyplot as plt


N=np.random.uniform(0,100,1000)
N=np.sort(N)
t=-5700*np.log(N/100)/np.log(2)
plt.title("Carbon 14 Decay")
plt.xlabel("Percentage of carbon 14 remaining")
plt.ylabel("Age of material")
plt.plot(N,t,"b-")

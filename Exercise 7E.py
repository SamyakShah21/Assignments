import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
temp=pd.read_csv("UKTemperature.csv")
plt.xlabel("Year")
plt.ylabel("Mean Temperature (degree Celsius)")
plt.title("Mean temperature in the UK")
x=np.array(temp.iloc[:,0])
y1=np.array(temp.iloc[:,13])
y2=np.array(np.sum(np.array(temp.iloc[:,1:13]),axis=1)/12)

plt.plot(x,y1,label="Annual")
plt.plot(x,y2,label="Mean using months")
plt.legend(loc="Upper left")
plt.xlim(1920,2010)

plt.ylim(7.0,10.5)
plt.xticks([1920,1940,2000])
plt.savefig("my_first_plot.jpeg")


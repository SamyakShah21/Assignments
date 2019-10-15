# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:53:00 2019

@author: HP
"""

import matplotlib.pyplot as plt
x=(-3,-1,0,3,3)
y=(0,-2,0,-1,2)
plt.xlabel("relative x value from center star")
plt.ylabel("relative y value from center star")
plt.title("Sketch of the Cassiopeia star constalation")
plt.axis([-4,4,-3,3])
plt.grid()
plt.plot(x,y,"r-",x,y,"b*")          #is an alternate command possible here?
plt.show()

plt.plot(data[:,1][data[:,2]==2],data[:,2][data[:,2]==2],"g-",
             data[:,1][data[:,2]==2],data[:,2][data[:,2]==2],"g*",
             label="Bacillus cereus")
    plt.plot(data[:,1][data[:,2]==3],data[:,2][data[:,2]==3],"r-",
             data[:,1][data[:,2]==3],data[:,2][data[:,2]==3],"r^",
             label="Listeria")
    plt.plot(data[:,1][data[:,2]==4],data[:,2][data[:,2]==4],"y-",
             data[:,1][data[:,2]==4],data[:,2][data[:,2]==4],"yx",
             label="Brochothrix thermosphacta")
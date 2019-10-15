# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 18:38:36 2019

@author: Samyak Shah
"""

def convertTemperature(T, unitFrom, unitTo):
    if unitFrom=="Celsius":
        if unitTo=="Fahrenheit":
            T= 1.8*T+32
        else:
            T=T+273.15
    elif unitFrom=="Fahrenheit":
        if unitTo=="Celsius":
            T=(T-32)/1.8
        else:
            T=(T+459.67)/1.8
    else:
        if unitTo=="Celsius":
            T=T-273.15
        else:
            T=T*1.8-459.67
    return T

T=float(input("Please enter a temperature:"))
unitFrom=input("unit from?:")
unitTo=input("unitTo?:")
print("{:.0f} {:s} = {:.0f} {:s}".format(T,unitFrom,convertTemperature(T,unitFrom,unitTo),unitTo))

# s is used for strings
#d for decimal ie integer
#f is used for float

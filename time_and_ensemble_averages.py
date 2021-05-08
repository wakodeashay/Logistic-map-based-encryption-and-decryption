#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 21:17:02 2021

@author: ashay
"""

#Time average
import random
x=0
Sum=0
x0=0.75
for i in range(10000000):
    x=1.25*x0*(1-x0)
    x0=x
    Sum=Sum+x0
Sum/10000000    
s=0
#Ensmeble average
xk=0.75
for i in range(100000):
    x0=random.random()
    for j in range(5000):
        x=1.25*xk*(1-xk)
        xk=x
    s=s+x
s/100000
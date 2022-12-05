# -*- coding: utf-8 -*-
import math
x = float(input())
y = float(input())
z = float(input())
t = float(input())
c = math.sqrt(x*x+y*y)
def Square1(x, y):
     return x*y*0.5
def Square2(c, z, t):
     p = (z+t+c)/2
     return math.sqrt(p*(p-z)*(p-t)*(p-c))
print(Square1(x,y)+Square2(c,z,t))
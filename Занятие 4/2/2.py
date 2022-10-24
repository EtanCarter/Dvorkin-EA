# -*- coding: utf-8 -*-
a = int(input("1:"))
b = int(input("2:"))
if b > a:    
    for i in range(a, b+1):
         print(i)
else:
    for i in range (b, a+1):
         print(i)
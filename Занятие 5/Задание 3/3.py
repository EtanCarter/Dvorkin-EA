# -*- coding: utf-8 -*-
a = int(input())
b = 1
while (2**b) <= a:
    b+=1
print(b-1,2**(b-1))
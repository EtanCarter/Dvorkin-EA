# -*- coding: utf-8 -*-
n = int(input())
if n <1440:
    a=n//60
    b=n%60
    print(a,b)
else:
    while n>1440:
        n=n-1440
    g=n//60
    c=n%60
    print(g,c)

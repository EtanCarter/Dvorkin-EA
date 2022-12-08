#-*- coding: utf-8 -*-
def F():
    a = int(input())
    if a == 0:
        return int()
    return max([a, F()])
print(F())
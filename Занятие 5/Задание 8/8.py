# 6-8 Задания построены на коде из Задания 5
# -*- coding: utf-8 -*-
a = int(input())
b = 0
c = a
while a != 0:
    if a == c:
        b += 1
        a = c
    else:
        a = c
    a = int(input())
print(b)
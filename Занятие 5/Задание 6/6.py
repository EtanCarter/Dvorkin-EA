# Я взял программу из Задания 5 и чуть-чуть изменил
# -*- coding: utf-8 -*-
a = int(input())
b = 0
c = 0
while a != 0:
    c += a
    a = int(input())
    b += 1
print(c)
c = c / b
print(c)
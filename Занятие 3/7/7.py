# -*- coding: utf-8 -*-
s = int(input())
if (s%4==0 and s%100!=0) or s%400==0:
    print('да')
else:
    print('нет')

# -*- coding: utf-8 -*-
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
maxi = a.index(max(a))
mini = a.index(min(a))
maxin = a.pop(maxi)
minin = a.pop(mini)
a.insert(maxi, minin)
a.insert(mini, maxin)
print(a)
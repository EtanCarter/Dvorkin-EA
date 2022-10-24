Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # -*- coding: utf-8 -*-
... import math
... x = float(0.1722)
... y = float(6.33)
... z = float(3.25 * math.pow(10,-4))
... s = (5 * math.atan(x)) - (-1/4 * math.acos(x) * (((x+3) * (abs(x-y)) + (math.pow(x,2))) / ((abs(x-y)) * ((math.pow(x,2)) + z))))

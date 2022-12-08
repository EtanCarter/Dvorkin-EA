#-*- coding: utf-8 -*-
file = open(r"C:\Users\EthanCarter\Desktop\Dvorkin.E.A_Y-224_vvod1.txt",encoding='utf-8')
v = open(r"C:\Users\EthanCarter\Desktop\Dvorkin.E.A_Y-224_vvod1.txt",encoding='utf-8')
vv = open(r"C:\Users\EthanCarter\Desktop\Dvorkin.E.A_Y-224_vivod1.txt", 'w+',encoding='utf-8')
T = v.readlines()
O = file.readlines(5)
N = file.readlines()
a = [int(x) for x in T]
b = [int(x) for x in O]
z = [int(x) for x in N]
def F(c,d):
    vv.write('number:')
    for i in b:
        if i == c:
            vv.write('0')
            break
    for i in z:
        if i == c:
            vv.write('1')
            break
    vv.write('\n')
    for i in a:
        if i == c:
            i *= d
            vv.write(str(i))
        else:
            vv.write(str(i))
    vv.write('\n')
F(2,3)
vv.close() 

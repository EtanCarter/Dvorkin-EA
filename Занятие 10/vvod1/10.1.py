#-*- coding: utf-8 -*-
file = open(r"C:\Users\EthanCarter\Desktop\Dvorkin.E.A_Y-224_vvod1.txt",encoding='utf-8')
file2 = open(r"C:\Users\EthanCarter\Desktop\Dvorkin.E.A_Y-224_vivod1.txt", 'w+',encoding='utf-8')
T = file.readlines()
O = file2.readlines(5)
N = file2.readlines()
a = [int(x) for x in T]
b = [int(x) for x in O]
z = [int(x) for x in N]
def F(c,d):
    file2.write('number:')
    for i in b:
        if i == c:
            file2.write('0')
            break
    for i in z:
        if i == c:
            file2.write('1')
            break
    file2.write('\n')
    for i in a:
        if i == c:
            i *= d
            file2.write(str(i))
        else:
            file2.write(str(i))
    file2.write('\n')
F(2,3)
file2.close() 

#-*- coding: utf-8 -*-
file1 = open(r"C:\Users\EthanCarter\Desktop\Dvorkin.E.A_Y-224_vvod2.txt",encoding='utf-8')
file2 = open(r"C:\Users\EthanCarter\Desktop\Dvorkin.E.A_Y-224_vivod2.txt", 'w+',encoding='utf-8')
T = file1.readlines()
O = file1.readlines(7)
N = file1.readlines(5)
P = file1.readlines(5)
def F(e,a,b,z):
    N = []
    for i in a:
        if i % 2 == 1:
            s = sum(a)
            N.append(s)
    for i in b:
        if i % 2 == 1:
            s = sum(b)
            N.append(s)
    for i in z:
        if i % 2 == 1:
            s = sum(z)
            N.append(s)
    for y in range(3):
        if sum(a) == max(N):
            file2.write('0')
            break
        if sum(b) == max(N):
            file2.write('1')
            break
        if sum(z) == max(N):
            file2.write('2')   
            break
    file2.write('\n')
    file2.write(str(max(N)))
F(([int(x) for x in T]),([int(x) for x in O]),([int(x) for x in N]),([int(x) for x in P]))
file2.close()

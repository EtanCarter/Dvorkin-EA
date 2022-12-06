# -*- coding: utf-8 -*-
def D():
    b = int(input()) #размер матрицы
    k = (b*b - b)//2 + b
    print()
    n = []
    for i in range(b):
        n.append([0]*b)
        for j in range(i,b):
            n[i][j] = int(input(':'))
    for i in range(b):
        for j in range(i,b):
            n[j][i] = n[i][j]
    for row in n:
        print(row, sep='\t')
print(D())
# -*- coding: utf-8 -*-
def mat(matrix):
    n=len(matrix)
    a=[]
    for i in range(n):
        a.append(matrix[i][i])
    return a
print(mat('9'))
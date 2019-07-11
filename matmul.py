import numpy as np
import csv
# read matrix A from 'A.csv'
a = open('A.csv','r')
A = []
for  line in a.readlines():
    A.append( [ float(x) for x in line.strip().split(',') ] )
a.close
print('A = ',A)
# read matrix B from 'B.csv'
b = open('b.csv','r')
B = []
for  line in b.readlines():
    B.append( [ float(x) for x in line.strip().split(',') ] )
b.close
print('B = ',B)

# find the result of c = A x b
def matmul(A,b):
    m,n = len(A), len(b[0])
    J = len(A[0])
    if len(A[0]) == len(b):
        C = [[0]*n for i in range(m)]
        for r in range(m):
            for c in range(n):
                C[(r)][c] = sum([ A[r][j] * b[j][c] for j in range(J) ])
            return C 
        return []
        
# print(C)
print('C = ',matmul(A,B))
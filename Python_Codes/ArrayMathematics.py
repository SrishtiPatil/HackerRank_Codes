import numpy as np
r,c = map(int,input().split())
ip=[]
for i in range(r):
    ip.append(input())
matrix1 = np.array([ip[i].split() for _ in range(n)], int)

n,m = map(int,input().split())
matrix1 = np.array([input().split() for _ in range(n)], int)
matrix2 = np.array([input().split() for i in range(n)], int)
print(np.add(matrix1,matrix2))
print(np.subtract(matrix1,matrix2))
print(np.multiply(matrix1,matrix2))
print(matrix1//matrix2)#Used to get integer division
print(np.mod(matrix1,matrix2))
print(np.power(matrix1,matrix2))

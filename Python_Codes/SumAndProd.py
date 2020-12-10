import numpy as np
n,m = map(int,input().split())
matrix1 = np.array([input().split() for _ in range(n)], int)
print(np.prod((np.sum(matrix1,axis=0))))

import numpy as np
n,m = map(int,input().split())
matrix1 = np.array([input().split() for _ in range(n)], int)
np.reshape(matrix1,(n,m))
minimum=[]
for i in range(n):
    minimum.append(np.min(matrix1,axis=1))
temp=np.max(minimum)
print(temp)

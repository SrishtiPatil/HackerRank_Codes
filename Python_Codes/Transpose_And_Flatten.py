import numpy as np
data = []
n, m = map(int, input().split())
for _ in range(n):
    data.append(list(map(int, input().split())))
arr = np.array(data)
print(np.transpose(arr))
print(arr.flatten())

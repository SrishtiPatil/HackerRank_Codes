import numpy as np
n = int(input())
list1 =list(map(int,input().split()))[:n]
m=max(list1)
list1.sort()
list1.reverse()
for i in list1:
    if i==m:
        continue
    else:
        m=i
        break
print(m)

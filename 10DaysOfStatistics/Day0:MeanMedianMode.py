# Day One : Mean Median Mode
from scipy import stats as sp
import numpy as np
n= int(input())
a=list(map(int,input().split()))
print(np.mean(a))
print(np.median(a))
print(int(sp.mode(a)[0]))

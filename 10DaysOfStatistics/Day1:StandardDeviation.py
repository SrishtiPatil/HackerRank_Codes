#Standard deviation
import math
n=int(input())
a=list(map(int,input().split()))
m=sum(a)/len(a)
t=0
for i in a:
    c=i-m
    c=c*c
    t+=c
b=t/len(a)
b=math.sqrt(b)
print("{0:.1f}".format(b))

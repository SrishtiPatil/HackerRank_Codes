# Enter your code here. Read input from STDIN. Print output to STDOUT
xy = [map(int, input().split()) for _ in range(5)]
sx=0
sy=0
sxSqr=0
sxy=0
for i,j in xy:
    sx+=i
    sy+=j
    sxSqr+=i**2
    sxy+=i*j
b = (5*sxy-sx*sy)/(5*sxSqr-sx**2)
a = (sy/5)-b*(sx/5)
ans=a+b*80
print("{0:.3f}".format(ans))

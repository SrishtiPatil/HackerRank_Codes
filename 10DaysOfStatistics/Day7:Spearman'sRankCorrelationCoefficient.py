# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
x=list(map(float,input().split()))
y=list(map(float,input().split()))
tx=sorted(x)
ty=sorted(y)
rankx=[]
ranky=[]
for i,j in zip(x,y):
    rankx.append(1+(tx.index(i)))
    ranky.append(1+(ty.index(j)))
d=[]
dsqr=[]
for i in range(n):
    a=rankx[i]-ranky[i]
    d.append(a)
    dsqr.append(a**2)

ans=1-((6*sum(dsqr))/(n*(n**2-1)))
print("{0:.3f}".format(ans))

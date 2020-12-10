# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
x=list(map(float,input().split()))
y=list(map(float,input().split()))
import statistics as st
mx=st.mean(x)
my=st.mean(y)
sx=st.pstdev(x)
sy=st.pstdev(y)
temp=0
for i in range(n):
    temp+=(x[i]-mx)*(y[i]-my)
ans=temp/(n*sx*sy)
print("{0:.3f}".format(ans))

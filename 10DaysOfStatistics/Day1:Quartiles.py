import statistics as st
n= int(input())
x=list(map(int,input().split()))
x=sorted(x)
m=int(n/2)  
print(int(st.median(x[:m])))
print(int(st.median(x)))
n=n+1
m=int(n/2)
print(int(st.median(x[m:])))

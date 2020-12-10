na=int(input())
a=set(map(int,input().split()))
nb=int(input())
b=set(map(int,input().split()))
c=a.symmetric_difference(b)
c=sorted(c)
for i in c:
    print(i)

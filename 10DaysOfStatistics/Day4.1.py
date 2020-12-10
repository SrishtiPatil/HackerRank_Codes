# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b=list(map(float,input().split(" ")))
x=int(input())
p=a/b
ans=0
for i in range(1,6):
    ans+=((1-p)**(i-1))*p
print("{0:.3f}".format(ans))

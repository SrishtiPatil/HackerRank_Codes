# Enter your code here. Read input from STDIN. Print output to STDOUT
a, b=list(map(float,input().split(" ")))
x=int(input())
p=a/b
ans=((1-p)**(x-1))*p
print("{0:.3f}".format(ans))

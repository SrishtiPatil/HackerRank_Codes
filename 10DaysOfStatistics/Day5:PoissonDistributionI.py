# Enter your code here. Read input from STDIN. Print output to STDOUT
def factorial(n):
    if n == 0:
        return 1 
    else:
        return n*factorial(n-1)
mean=float(input())
x=int(input())
import math as mt
ans=((mt.e**-mean)*(mean**x))/factorial(x)
print("{0:.3f}".format(ans))

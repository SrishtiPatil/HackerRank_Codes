# Enter your code here. Read input from STDIN. Print output to STDOUT
import math as mt
n=int(input())
x=int(input())
mu=float(input())
stdv=float(input())
    
mean = mu*x
b = stdv*mt.sqrt(x)
def clt(n, mean, b):
    return 0.5 * (1 + mt.erf((n - mean) / (b * (2 ** 0.5))))

print(round(clt(n, mean, b), 4))

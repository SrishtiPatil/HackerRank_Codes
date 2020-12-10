# Enter your code here. Read input from STDIN. Print output to STDOUT
def factorial(n):
    if n == 0:
        return 1 
    else:
        return n*factorial(n-1)

def combination(n, x):
    return factorial(n) / (factorial(x) * factorial(n-x))

def binomial(x, n, p):
    return combination(n, x) * p**x * (1-p)**(n-x)

l, r = list(map(float, input().split(" ")))
p = l / (l+r)
s=0
for i in range (3,7):
    s+=binomial(i,6,p)
print("{0:.3f}".format(s))

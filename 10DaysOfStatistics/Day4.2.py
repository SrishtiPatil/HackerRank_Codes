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

l, n = list(map(float, input().split(" ")))
p = l/100
s=0
for i in range (0,3):
    s+=binomial(i,10,p)
print("{0:.3f}".format(s))
s=0
for i in range (2,11):
    s+=binomial(i,10,p)
print("{0:.3f}".format(s))

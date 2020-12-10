# Enter your code here. Read input from STDIN. Print output to STDOUT
import math as mt
n=int(input())
mu=int(input())
sigma=int(input())
p=float(input())
z=float(input())
stdDev=mu/mt.sqrt(n)
lowerBound=mu-((z*sigma)/mt.sqrt(n))
upperBound=mu+((z*sigma)/mt.sqrt(n))
print(round(lowerBound, 4))
print(round(upperBound, 4))

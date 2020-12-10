# Enter your code here. Read input from STDIN. Print output to STDOUT
mean1, mean2=list(map(float,input().split()))
ans1=160+40*(mean1+(mean1**2))
ans2=128+40*(mean2+(mean2**2))
print("{0:.3f}".format(ans1))
print("{0:.3f}".format(ans2))

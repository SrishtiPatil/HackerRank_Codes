# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int, input().split())
if n>5 and n<101 and m>15 and m<303 and m==3*n and n%2!=0:
    dash=m-3
    c=0
    for i in range(int(n/2)):
        for j in range(int(dash/2)):
            print("-",end="")
        for k in range((2*i)+1):
            print(".|.",end="")
            c=(2*i)+1
        for l in range(int(dash/2)):
            print("-",end="")
        print()
        dash=dash-6
    dash=m-7
    for j in range(int(dash/2)):
        print("-",end="")
    print("WELCOME",end="")
    for j in range(int(dash/2)):
        print("-",end="")
    print()
    dash=3
    z=0
    for i in range(int(n/2)):
        for j in range(dash):
            print("-",end="")
        for k in range(c):
            print(".|.",end="")
        c=c-2
        for l in range(dash):
            print("-",end="")
        dash=dash+3
        print()

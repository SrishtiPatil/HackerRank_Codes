#

def nextMove(n,r,c,grid):
    for i,j in enumerate(grid):
        if 'p' in j:
            spot_p=(i,j.index('p'))
    row_diff=r-spot_p[0]
    col_diff=c-spot_p[1]
    if row_diff<0:
        return "DOWN"
    elif row_diff>0:
        return "UP"
    elif col_diff<0:
        return "RIGHT"
    else:
        return "LEFT"


n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))

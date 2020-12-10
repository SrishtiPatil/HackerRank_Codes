def nextMove(posr, posc, board):
    for i,j in enumerate(board):
        if 'd' in j:
            spot_d=(i,j.index('d'))
    row_diff=posr-spot_d[0]
    col_diff=posc-spot_d[1]
    if row_diff==0 and col_diff==0:
        print("CLEAN")
    elif row_diff<0:
        print("DOWN")
    elif row_diff>0:
        print("UP")
    elif col_diff<0:
        print("RIGHT")
    else:
        print("LEFT")

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
    
    
    

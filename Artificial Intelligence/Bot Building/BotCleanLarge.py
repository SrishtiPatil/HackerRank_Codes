
def next_move(posr, posc, dimx, dimy, board):
    spot_d=[]
    for i,j in enumerate(board):
        for k in range(len(j)):
            if 'd' == j[k]:
                spot_d.append([i, k])
    #spot_d=np.reshape(spot_d, (round(len(spot_d)/2),2))
    dist=[]

    for i in range(len(spot_d)):
        dist.append(abs(posr-spot_d[i][0])+abs(posc-spot_d[i][1]))
    for i in range(len(dist)):
        min_d=dist.index(min(dist))
        if i==1:
            break
        for k in range(dist[min_d]+1):
            row_diff=posr-spot_d[min_d][0]
            col_diff=posc-spot_d[min_d][1]
            if row_diff==0 and col_diff==0:
                print("CLEAN")
                if len(dist)!=0:
                    dist[min_d]= max(dist)+1
                    break
            elif col_diff<0:
                print("RIGHT")
                posc+=1
                break
            elif col_diff>0:
                print("LEFT")
                posc-=1
                break
            elif row_diff<0:
                print("DOWN")
                posr+=1
                break
            else:
                print("UP")
                posr-=1
                break
            
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)

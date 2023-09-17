# Shortest Bridge
# 2 Islands----> Connect with minimum number of flips to 0s

from collections import deque


def ShortestBridge(n,grid):
    dq=deque()
    flag=True
    for i in range(n):
        for j in range(n):
            if grid[i][j]==1 and flag==True:
                dq.append([i,j])
                flag=False
                grid[i][j]=2
    
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    while dq:
        i,j=dq.popleft()
        for k in range(4):
            row=dx[k]+i
            col=dy[k]+j
            if row>=0 and row<n and col>=0 and col<n and grid[row][col]==1:
                grid[row][col]=2
                dq.append([row,col])
    for i in range(n):
        for j in range(n):
            if grid[i][j]==2:
                dq.append([i,j])
    level=-1
    while dq:
        size=len(dq)
        level+=1
        for _ in range(size):
            i,j=dq.popleft()
            for k in range(4):
                row=dx[k]+i
                col=dy[k]+j
                if row>=0 and row<n and col>=0 and col<n and grid[row][col]!=2:
                    if grid[row][col]==1:
                        return level
                    else:
                        grid[row][col]=2
                        dq.append([row,col])
    return -1

def main():
    n=int(input())
    grid=[]
    for i in range(n):
        grid.append(list(map(int,input().split())))
    ans=ShortestBridge(n,grid)
    print(ans)


if __name__=='__main__':
    main()
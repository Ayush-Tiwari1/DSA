# As Far from Land as Possible

from collections import deque

def AsFarFromLand(n,grid):
    dq=deque()
    one=False
    zero=False
    for i in range(n):
        for j in range(n):
            if grid[i][j]==1:
                dq.append([i,j])
                one=True
            if grid[i][j]==0:
                zero=True
    if one==False or zero==False:
        return -1
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    level=-1
    while dq:
        size=len(dq)
        level+=1
        for _ in range(size):
            i,j=dq.popleft()
            for k in range(4):
                row=dx[k]+i
                col=dy[k]+j
                if row>=0 and row<n and col>=0 and col<n and grid[row][col]==0:
                    dq.append([row,col])
                    grid[row][col]=1
    
    return level


def main():
    n=int(input())
    grid=[]
    for i in range(n):
        grid.append(list(map(int,input().split())))
    ans=AsFarFromLand(n,grid)
    print(ans)


if __name__=='__main__':
    main()
    
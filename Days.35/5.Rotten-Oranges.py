# Rotten Oranges


'''
0 ----> Empty Cell
1 ----> Fresh Oranges
2 ----> Rotten Oranges
'''

from collections import deque

def RottenOranges(m,n,grid):
    dq=deque()
    is_fresh=False
    for i in range(m):
        for j in range(n):
            if grid[i][j]==2:
                dq.append([i,j])
            if grid[i][j]==1:
                is_fresh=True
    
    # No Fresh Elements ----> therefore 0 minutes to rot all fresh oranges
    if is_fresh==False:
        return 0
    time=-1

    dx=[-1,0,1,0]
    dy=[0,1,0,-1]

    while dq:
        size=len(dq)
        time+=1
        for t in range(size):
            i,j=dq.popleft()
            for k in range(4):
                row=dx[k]+i
                col=dy[k]+j
                if row>=0 and row<m and col>=0 and col<n and grid[row][col]==1:
                    grid[row][col]=2
                    dq.append([row,col])

    for i in range(m):
        for j in range(n):
            if grid[i][j]==1:
                return -1

    return time


def main():
    m,n=map(int,input().split())
    grid=[]
    for i in range(m):
        grid.append(list(map(int,input().split())))
    
    time=RottenOranges(m,n,grid)
    if time==-1:
        print('Not Possible to Rot all oranges')
    else:
        print('Time to rotten all Oranges:',time)


if __name__=="__main__":
    main()

from queue import Queue

def isValid(i,j,n,m,grid):
    if i<0 or j<0 or i>=n or j>=m or grid[i][j]!=1:
        return False
    return True

def RottenOranges(grid,n,m):
    time=0
    q=Queue()
    for i in range(n):
        for j in range(m):
            if grid[i][j]==2:
                q.put([i,j])
    dx=[1,-1,0,0]
    dy=[0,0,-1,1]
    while q.qsize()>0:
        currsize=q.qsize()
        flag=0
        for _ in range(currsize):
            temp=q.get()
            i=temp[0]
            j=temp[1]
            for indx in range(4):
                if isValid(i+dx[indx],j+dy[indx],n,m,grid)==True:
                    flag=1
                    q.put([i+dx[indx],j+dy[indx]])
                    grid[i+dx[indx]][j+dy[indx]]=2
        if flag==1:
            time+=1
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1:
                return -1
    return time

def main():
    n,m=map(int,input().strip().split())
    grid=[]
    for _ in range(n):
        grid.append(list(map(int,input().strip().split())))
    ans=RottenOranges(grid,n,m)
    if ans==-1:
        print('Not Possible to Rotten All Oranges')
    else:
        print('Time to Rotten All Oranges:',ans)


main()
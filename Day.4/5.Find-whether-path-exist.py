

def main():
    def DFS(row,col,n,grid,visited):
        if row<0 or col<0 or row>=n or col>=n or grid[row][col]==0 or visited[row][col]==True:
            return False
        if grid[row][col]==2:
            return True
        visited[row][col]=True
        v1=DFS(row+1,col,n,grid,visited)
        v2=DFS(row,col+1,n,grid,visited)
        v3=DFS(row-1,col,n,grid,visited)
        v4=DFS(row,col-1,n,grid,visited)
        return v1 or v2 or v3 or v4
        
    n=int(input())
    grid=[]
    for i in range(n):
        grid.append(list(map(int,input().split())))
    visited=[[False]*n for i in range(n)]
    row=col=None
    for i in range(n):
        for j in range(n):
            if grid[i][j]==1:
                row=i
                col=j
                break
            
    ans=DFS(row,col,n,grid,visited)
    if ans == True:
        print(1)
    else:
        print(0)

if __name__=='__main__':
    main()
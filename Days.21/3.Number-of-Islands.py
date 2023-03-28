def dfs(i,j,n,m,grid,visited):
    if i<0 or j<0 or i>=n or j>=m or grid[i][j]==0 or visited[i][j]==True:
        return
    visited[i][j]=True
    dfs(i-1,j,n,m,grid,visited)
    dfs(i+1,j,n,m,grid,visited)
    dfs(i,j-1,n,m,grid,visited)
    dfs(i,j+1,n,m,grid,visited)
    dfs(i-1,j-1,n,m,grid,visited)
    dfs(i-1,j+1,n,m,grid,visited)
    dfs(i+1,j-1,n,m,grid,visited)
    dfs(i+1,j+1,n,m,grid,visited)

def numIslands(grid):
    n=len(grid)
    m=len(grid[0])
    visited=[[False for j in range(m)] for i in range(n)]
    count=0
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1 and visited[i][j]==False:
                count+=1
                dfs(i,j,n,m,grid,visited)
    return count

if __name__=='__main__':
    n,m=map(int,input().split())
    grid=[]
    for i in range(n):
        grid.append(list(map(int,input().strip().split())))
    islands=numIslands(grid)
    print('Islands:',islands)
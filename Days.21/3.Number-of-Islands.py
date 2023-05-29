
def main():
    def dfs(i,j,n,m,visited,grid):
        if i<0 or j<0 or i>=n or j>=m or visited[i][j]==True or grid[i][j]==0:
            return
        visited[i][j]=True
        dfs(i+1,j,n,m,visited,grid)
        dfs(i,j+1,n,m,visited,grid)
        dfs(i-1,j,n,m,visited,grid)
        dfs(i,j-1,n,m,visited,grid)
        dfs(i-1,j-1,n,m,visited,grid)
        dfs(i-1,j+1,n,m,visited,grid)
        dfs(i+1,j-1,n,m,visited,grid)
        dfs(i+1,j+1,n,m,visited,grid)
    n,m=map(int,input().strip().split())
    grid=[[] for i in range(n)]
    for i in range(n):
        grid[i]=list(map(int,input().strip().split()))
    for i in range(n):
        for j in range(m):
            print(grid[i][j],end=" ")
        print()
    count=0
    visited=[[False for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if visited[i][j]==False and grid[i][j]==1:
                count+=1
                dfs(i,j,n,m,visited,grid)
    print('Number of Islands: ',count)



main()
# Coloring a Border

# Edge Case:
'''
    2  2  2
    2 |2| 2
    2  2  2
    
    |2| ---> Don't Change it's color, as it is surrounded by all 2s.
'''


'''
Input:
# m n
3 3  
1 1 1
1 1 1
1 1 1
#row col color
1 1 2

Output:
2 2 2 
2 1 2 
2 2 2 
'''

def isValid(i,j,m,n,oldColor,grid):
    if i<0 or j<0 or i>=m or j>=n or abs(grid[i][j])!=oldColor:
        return False
    return True

def dfs(row,col,m,n,oldColor,visited,grid):
    count=0
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    grid[row][col]=-oldColor
    visited[row][col]=True

    for i in range(4):
        if isValid(dx[i]+row,dy[i]+col,m,n,oldColor,grid):
            count+=1
            if grid[dx[i]+row][dy[i]+col]>0 and visited[dx[i]+row][dy[i]+col]==False:
                dfs(dx[i]+row,dy[i]+col,m,n,oldColor,visited,grid)
        
    if count==4:
        grid[row][col]=oldColor

def ColorBorder(row,col,color,m,n,grid):
    
    newColor=color
    oldColor=grid[row][col]
    if newColor==oldColor:
        return grid
    
    visited=[[False for j in range(n)] for i in range(m)]
    dfs(row,col,m,n,oldColor,visited,grid)
    
    for i in range(m):
        for j in range(n):
            if grid[i][j]<0:
                grid[i][j]=newColor
    return grid
    
def main():
    m,n=map(int,input().split())
    grid=[]
    for i in range(m):
        grid.append(list(map(int,input().split())))
    
    row,col,color=map(int,input().split())
    
    ans=ColorBorder(row,col,color,m,n,grid)
    
    for i in range(m):
        for j in range(n):
            print(ans[i][j],end=" ")
        print()



if __name__=='__main__':
    main()


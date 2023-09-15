# Number of Distinct Islands
'''
Positions:

        U
        |
    L - M - R
        |
        D

M ---> Main/Current Location

U ---> Up
R ---> Right
D ---> Down
L ---> Left
B ---> BackTract

As:
1 1
1 0
it is --> MRD

1 1
0 1
it is --> MRD

Both are same, but structure is different
therefore, we will add B whenever we BackTrack

1 1
1 0
it is --> MRBDB

1 1
0 1
it is --> MRDBB
'''

def dfs(i,j,m,n,path,visited,grid):
    visited[i][j]=True
    
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    dir=['U','R','D','L']
    for t in range(4):
        row=dx[t]+i
        col=dy[t]+j
        if row>=0 and row<m and col>=0 and col<n and visited[row][col]==False and grid[row][col]==1:
            path+=dir[t]
            dfs(row,col,m,n,path,visited,grid)
            path+='B'
    

def main():
    m,n=map(int,input().split())
    grid=[]
    for i in range(m):
        grid.append(list(map(int,input().split())))
    visited=[[False for j in range(n)] for i in range(m)]
    dict={}
    count=0
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1 and visited[i][j]==False:
                path="M"
                dfs(i,j,m,n,path,visited,grid)
                if path not in dict:
                    count+=1
                    dict[path]=True
    print('Number of Distinct Islands:',count)



if __name__=='__main__':
    main()
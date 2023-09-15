# Zero-One Matrix

from collections import deque

def ZeroOne(m,n,matrix):
    dq=deque()
    
    visited=[[False for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                dq.append([i,j])
                visited[i][j]=True
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    while dq:
        i,j=dq.popleft()
        for k in range(4):
            row=dx[k]+i
            col=dy[k]+j
            if row>=0 and row<m and col>=0 and col<n and visited[row][col]==False:
                matrix[row][col]=matrix[i][j]+1
                dq.append([row,col])
                visited[row][col]=True

def main():
    m,n=map(int,input().split())
    matrix=[]
    for i in range(m):
        matrix.append(list(map(int,input().split())))
    ZeroOne(m,n,matrix)
    for i in range(m):
        for j in range(n):
            print(matrix[i][j],end=" ")
        print()


if __name__=='__main__':
    main()
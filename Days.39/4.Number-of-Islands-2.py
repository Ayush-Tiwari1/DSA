# Number of Islands-2

# Dynamic Graph -----> DSU (Disjoint Set Union)

'''
n*m--> 3*5
    0 1 2 3 4
  -------------
0 | 0 0 0 0 0 |
1 | 0 0 0 0 0 |
2 | 0 0 0 0 0 |
  -------------

we will assume above indices as :
    0   1   2   3   4
  ----------------------
0 | 0   1   2   3   4  |
1 | 5   6   7   8   9  |
2 | 10  11  12  13  14 |
  ----------------------

conversion from (row,col) ----> DSU index

index=(m*row+col)

'''


# Find by Path Compression
def Find(u,parent):
    if parent[u]==-1:
        return u
    parent[u]=Find(parent[u],parent)
    return parent[u]


# Union By Rank
def Union(x,y,rank,parent):
    if rank[x]==rank[y]:
        parent[y]=x
        rank[x]+=1
    elif rank[x]>rank[y]:
        parent[y]=x
    else:
        parent[x]=y


def NumberofIslands2(n,m,queries):
    V=n*m
    grid=[[0 for j in range(V)] for i in range(V)]
    parent=[-1 for i in range(V)]
    rank=[0 for i in range(V)]
    ans=[]
    count=0
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    
    for row,col in queries:
        indx=m*row+col
        grid[row][col]=1
        count+=1
        for k in range(4):
            # Neighbors
            i=row+dx[k]
            j=col+dy[k]
            
            if i>=0 and i<V and j>=0 and j<V and grid[i][j]==1:
                x=Find(indx,parent)
                y=Find(m*i+j,parent)
                if x!=y:
                    Union(x,y,rank,parent)
                    count-=1
        ans.append(count)
    return ans


def main():
    n,m,q=map(int,input().split())
    queries=[]
    for i in range(q):
        queries.append(list(map(int,input().split())))
    ans=NumberofIslands2(n,m,queries)
    print('Number of Islands at each queries:')
    for val in ans:
        print(val,end= " ")


if __name__=='__main__':
    main()
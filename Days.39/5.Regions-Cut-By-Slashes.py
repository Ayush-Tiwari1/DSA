# Regions Cut By Slashes
# / \ ' '
# \ ---> represented as \\ for input because \ termed as escaped


# Find By Path Compression
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



def RegionsCutBySlashes(grid):
    n=len(grid)+1
    # Disjoint Set Union
    parent=[-1 for i in range(n*n)]
    rank=[0 for i in range(n*n)]
    ans=1
    # Union all boundaries 
    # i=0
    for j in range(1,n):
        Union(0,j,rank,parent)
    # i=n-1
    for j in range(1,n):
        indx=n*(n-1)+j
        Union(0,indx,rank,parent)
    # j=0
    for i in range(1,n):
        indx=n*i
        Union(0,indx,rank,parent)
    # j=n-1
    # Last Element already merge at i==n-1
    for i in range(1,n-1):
        indx=i*n+(n-1)
        Union(0,indx,rank,parent)
    for i in range(n-1):
        for j in range(len(grid[i])):
            if grid[i][j]=='/':
                indx1=n*(i+1)+j
                indx2=n*i+(j+1)
                x=Find(indx1,parent)
                y=Find(indx2,parent)
                if x!=y:
                    Union(x,y,rank,parent)
                else:
                    ans+=1
            elif grid[i][j]=='\\':
                indx1=n*i+j
                indx2=n*(i+1)+(j+1)
                x=Find(indx1,parent)
                y=Find(indx2,parent)
                if x!=y:
                    Union(x,y,rank,parent)
                else:
                    ans+=1
    return ans
        



def main():
    n=int(input())
    grid=[]
    for i in range(n):
        grid.append(input())
    print(grid)
    ans=RegionsCutBySlashes(grid)
    print('Regions Cut By Slashes are:',ans)


if __name__=='__main__':
    main()




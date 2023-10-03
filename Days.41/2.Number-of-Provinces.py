# Number of Provinces

# Find by Path Compression
def Find(u,parent):
    if parent[u]==-1:
        return u
    parent[u]=Find(parent[u],parent)
    return parent[u]


# Union by Rank
def Union(x,y,rank,parent):
    if rank[x]>rank[y]:
        parent[y]=x
    elif rank[x]<rank[y]:
        parent[x]=y
    else:
        parent[y]=x
        rank[x]+=1


def NumberofProvinces(isConnected):
    n=len(isConnected)
    parent=[-1 for i in range(n)]
    rank=[0 for i in range(n)]
    
    for i in range(n):
        for j in range(i+1,n):
            if isConnected[i][j]==1:
                x=Find(i,parent)
                y=Find(j,parent)
                if x!=y:
                    Union(x,y,rank,parent)
    ans=0
    for i in range(n):
        if parent[i]==-1:
            ans+=1
    return ans

def main():
    n=int(input())
    isConnected=[]
    for i in range(n):
        isConnected.append(list(map(int,input().split())))
    ans=NumberofProvinces(isConnected)
    print('Number of Provinces:',ans)



if __name__=='__main__':
    main()
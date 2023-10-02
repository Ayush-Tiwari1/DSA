# Redundant Connections

# Find by Path Compresssion
def Find(u,parent):
    if parent[u]==-1:
        return u
    parent[u]=Find(parent[u],parent)
    return parent[u]

# Union by Rank
def Union(x,y,rank,parent):
    if rank[x]==rank[y]:
        parent[y]=x
        rank[x]+=1
    elif rank[x]>rank[y]:
        parent[y]=x
    else:
        parent[x]=y


def RedundantConnections(edges):
    n=len(edges)
    # Disjoint Set Union
    ans=[]
    parent=[-1 for i in range(n)]
    rank=[0 for i in range(n)]
    for u,v in edges:
        x=Find(u-1,parent)
        y=Find(v-1,parent)
        if x!=y:
            Union(x,y,rank,parent)
        else:
            ans.append([u,v])
    return ans



def main():
    n=int(input())
    edges=[]
    for i in range(n):
        edges.append(list(map(int,input().split())))
    ans=RedundantConnections(edges)
    for edge in ans:
        print(edge)



if __name__=='__main__':
    main()
# Kruskal's Algorithm

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


def KruskalAlgorithm(V,E,Edges):
    Edges.sort(key=lambda edge: edge[2])
    parent=[-1 for i in range(V)]
    rank=[0 for i in range(V)]
    mst=[]
    for u,v,wt in Edges:
        x=Find(u,parent)
        y=Find(v,parent)
        if x!=y:
          mst.append([u,v,wt])  
          Union(x,y,rank,parent)
    return mst


def main():
    V,E=map(int,input().split())
    Edges=[]
    for i in range(E):
        Edges.append(list(map(int,input().split())))
    
    MST=KruskalAlgorithm(V,E,Edges)
    print('Minimum Spanning Tree:')
    for edge in MST:
        print(edge)



if __name__=='__main__':
    main()
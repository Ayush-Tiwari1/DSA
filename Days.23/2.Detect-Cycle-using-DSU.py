
def Find(u,parent):
    if parent[u]==u:
        return u
    parent[u]=Find(parent[u],parent)
    return parent[u]

def Union(a,b,parent,rank):
    if rank[a]>rank[b]:
        parent[b]=a
    elif rank[a]<rank[b]:
        parent[a]=b
    else:
        rank[a]+=1
        parent[b]=a

def DetectCycle(adj,V):
    parent=[int(i) for i in range(V)]
    rank=[0]*V
    for i in range(V):
        for j in range(len(adj[i])):
            if i<adj[i][j]:
                p1=Find(i,parent)
                p2=Find(adj[i][j],parent)
                if p1==p2:
                    return True
                else:
                    Union(p1,p2,parent,rank)
    return False

def main():
    V,E=map(int,input().split())
    adj=[[] for i in range(V)]
    for _ in range(E):
        u,v=map(int,input().split())
        adj[u].append(v)
        adj[v].append(u)
    ans=DetectCycle(adj,V)
    if ans==True:
        print('Cycle Present')
    else:
        print('Cycle is Not Present')


if __name__=='__main__':
    main()
#Detect Cycle using DSU

def main():
    def Find(u,parent):
        if parent[u]==-1:
            return u
        parent[u]=Find(parent[u],parent)
        return parent[u]
    
    def Union(x,y,parent,rank):
        if rank[x]==rank[y]:
            parent[y]=x
            rank[x]+=1
        elif rank[x]>rank[y]:
            parent[y]=x
        else:
            parent[x]=y
    
    def CycleDetection(V,adj):
        parent=[-1 for i in range(V)]
        rank=[0 for i in range(V)]
        for i in range(V):
            for j in range(len(adj[i])):
                if i<adj[i][j]:
                    x=Find(i,parent)
                    y=Find(adj[i][j],parent)
                    if x==y:
                        return True
                    Union(x,y,parent,rank)
        
        return False            
                    
    
    
    V,E=map(int,input().strip().split())
    adj=[[] for i in range(V)]
    for i in range(E):
        u,v=map(int,input().strip().split())
        adj[u].append(v)
        adj[v].append(u)
    print('Adjancency List:')
    for i in range(V):
        print(i,end=": ")
        for j in range(len(adj[i])):
            print(adj[i][j],end=" ")
        print()
    b=CycleDetection(V,adj)
    if b==True:
        print('Cycle Present')
    else:
        print('Cycle Not Present')

main()
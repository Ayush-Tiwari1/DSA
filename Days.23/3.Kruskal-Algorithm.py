#Kruskal's Algorithm ---> Using Disjoint Set Union

#Find by Path Compression--> O(logn)
def Find(u,parent):
    if parent[u]==u:
        return u
    parent[u]=Find(parent[u],parent)
    return parent[u]

#Union by Rank ---> O(logn)
def Union(a,b,parent,rank):
    if rank[a]>rank[b]:
        parent[b]=a
    elif rank[a]<rank[b]:
        parent[a]=b
    else:
        rank[a]+=1
        parent[b]=a

def Compare(List):
    return List[2]

def KruskalAlgorithm(adj,V):
    parent=[i for i in range(V)]
    rank=[-1 for i in range(V)]
    Edge =[]
    for i in range(V):
        for j in range(len(adj[i])):
            #I will consider 
            #Pair 0-----6
            #Not  6----0 again
            #Therefore, 0<6 (i<adj[i][j])
            if i<adj[i][j][0]:
                Edge.append([i,adj[i][j][0],adj[i][j][1]])
    Edge.sort(key=Compare)
    sum=0
    for i in range(len(Edge)):
        u=Edge[i][0]
        v=Edge[i][1]
        wt=Edge[i][2]
        
        #absolute parent1
        absp1=Find(u,parent)
        #absolute parent2
        absp2=Find(v,parent)
        if absp1!=absp2:
            Union(absp1,absp2,parent,rank)
            sum+=wt
    return sum

def main():
    V,E=map(int,input().split())
    adj=[[] for i in range(V)]
    for _ in range(E):
        u,v,wt=map(int,input().split())
        adj[u].append([v,wt])
        adj[v].append([u,wt])
    sum=KruskalAlgorithm(adj,V)
    print('Sum of Minimum Spanning Tree:',sum)
if __name__=='__main__':
    main()
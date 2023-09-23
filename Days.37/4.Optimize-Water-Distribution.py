# Optimize Water Distribution 
# Well dig or pipe with minimum cost

'''
Input:
5 6
1 2 2
1 4 12
2 4 8
2 3 4
2 5 14
3 5 7
3 9 12 10 6

Output:
23
'''



def Find(u,parent):
    if parent[u]==-1:
        return u
    parent[u]=Find(parent[u],parent)
    return parent[u]

def Union(x,y,rank,parent):
    if rank[x]==rank[y]:
        parent[y]=x
        rank[x]+=1
    elif rank[x]>rank[y]:
        parent[y]=x
    else:
        parent[x]=y


def OptimizeWaterDistribution(V,edges,wells):
    # create dummy node 0 and connect it with each vertices 
    # with wells dig cost
    for i in range(V):
        edges.append([0,i+1,wells[i]])
    
    # Apply Kruskal's Algorithm
    edges.sort(key=lambda x: x[2])
    ans=0
    parent=[-1 for i in range(V+1)]
    rank=[0 for i in range(V+1)]
    for u,v,wt in edges:
        x=Find(u,parent)
        y=Find(v,parent)
        if x!=y:
            # print(u,v,wt)
            Union(x,y,rank,parent)
            ans+=wt
    return ans

def main():
    V,E=map(int,input().split())
    edges=[]
    for i in range(E):
        edges.append(list(map(int,input().split())))
    wells=list(map(int,input().split()))
    ans=OptimizeWaterDistribution(V,edges,wells)
    print(ans)


if __name__=='__main__':
    main()
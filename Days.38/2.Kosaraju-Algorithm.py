# Kosaraju's Algorithm ----> Strongly Connected Component


def dfs(u,visited,topo,adj):
    visited[u]=True
    for v in adj[u]:
        if visited[v]==False:
            dfs(v,visited,topo,adj)
    topo.append(u)

def dfs2(u,visited,scc,adj):
    scc.append(u)
    visited[u]=True
    for v in adj[u]:
        if visited[v]==False:
            dfs2(v,visited,scc,adj)

def KosarajuAlgorithm(V,adj):
    topo=[]
    visited=[False for i in range(V)]
    
    # 1. Topographical Sort
    for i in range(V):
        if visited[i]==False:
            dfs(i,visited,topo,adj)
    
    topo.reverse()
    
    # 2. Reverse Edges of Graph
    adjlist=[[] for i in range(V)]
    for u in range(V):
        for v in adj[u]:
            adjlist[v].append(u)
    
    # 3. dfs using Topographical sort
    for i in range(V):
        visited[i]=False
    
    sccs=[]
    for i in topo:
        if visited[i]==False:
            scc=[]
            dfs2(i,visited,scc,adjlist)
            sccs.append(scc)
    return sccs
    


def main():
    V,E=map(int,input().split())
    adj=[[] for i in range(V)]
    for i in range(E):
        u,v=map(int,input().split())
        adj[u].append(v)
    sccs=KosarajuAlgorithm(V,adj)
    print('Strongly Connected Components:')
    for scc in sccs:
        print(scc)



if __name__=='__main__':
    main()
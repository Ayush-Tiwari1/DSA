
def main():
    def dfs(i,V,visited,topo,adj):
        visited[i]=True
        for j in range(len(adj[i])):
            if visited[adj[i][j]]==False:
                dfs(adj[i][j],V,visited,topo,adj)
        topo.append(i)
    E,V=map(int,input().strip().split())
    adj=[[] for i in range(V)]
    for i in range(E):
        u,v=map(int,input().strip().split())
        adj[u].append(v)
    topo=[]
    visited=[False for _ in range(V)]
    for i in range(V):
        if visited[i]==False:
            dfs(i,V,visited,topo,adj)
    topo.reverse()
    print(topo)


main()
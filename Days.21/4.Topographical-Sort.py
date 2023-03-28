
def Print(adj,V):
    for i in range(V):
        print(i," :",end=" ")
        for j in range(len(adj[i])):
            print(adj[i][j],end=" ")
        print()

def dfs(i,visited,adj,topo):
    visited[i]=True
    for j in range(len(adj[i])):
        if visited[adj[i][j]]==False:
            dfs(adj[i][j],visited,adj,topo)
    topo.append(i)

def TopographicalSort(adj,V):
    topo=[]
    visited=[False for i in range(V)]
    for i in range(V):
        if visited[i]==False:
            dfs(i,visited,adj,topo)
    topo.reverse()
    return topo

def main():
    E,V=map(int,input().split())
    adj=[[] for i in range(V)]
    for i in range(E):
        u,v=map(int,input().split())
        adj[u].append(v)
    Print(adj,V)
    topo=TopographicalSort(adj,V)
    for val in topo:
        print(val,end=" ")

if __name__ == '__main__':
    main()  
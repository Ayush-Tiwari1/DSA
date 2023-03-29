
def Print(adj,V):
    for i in range(V):
        print(i," :",end=" ")
        for j in range(len(adj[i])):
            print(adj[i][j],end=" ")
        print()

def dfs(adj,i,color,V,visited):
    visited[i]=color
    for j in range(len(adj[i])):
        if visited[adj[i][j]]==-1:
            newcolor=not color
            if dfs(adj,adj[i][j],newcolor,V,visited)==False:
                return False
        elif visited[adj[i][j]]==color:
            return False
    return True

def isGraphBipartite(adj,V):
    visited=[-1]*V
    for i in range(V):
        if visited[i]==-1:
            if dfs(adj,i,0,V,visited)==False:
                return False
    return True

def main():
    V,E=map(int,input().strip().split())
    adj=[[] for _ in range(V)]
    for _ in range(E):
        u,v=map(int,input().split())
        adj[u].append(v)
        adj[v].append(u)
    Print(adj,V)
    ans=isGraphBipartite(adj,V)
    if ans==True:
        print('Graph Bipartite')
    else:
        print('Graph Not Bipartite')

if __name__=='__main__':
    main()


def main():
    def DFS(i,V,adj,visited,ans):
        visited[i]=True
        ans.append(i)
        for j in range(len(adj[i])):
            if visited[adj[i][j]]==False:
                DFS(adj[i][j],V,adj,visited,ans)
    V,E=map(int,input().strip().split())
    adj=[[] for i in range(V)]
    for _ in range(E):
        u,v=map(int,input().strip().split())
        adj[u].append(v)
        adj[v].append(u)
    for i in range(V):
        print(i,end=":")
        for j in range(len(adj[i])):
            print(adj[i][j],end=" ")
        print()
    ans=[]
    visited=[False for _ in range(V)]
    for i in range(V):
        if visited[i]==False:
            DFS(i,V,adj,visited,ans)
    print('DFS:',end=" ")
    for val in ans:
        print(val,end=" ")

main()
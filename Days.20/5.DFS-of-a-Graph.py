
def Print(adj,V):
    for i in range(V):
        print(i," :",end=" ")
        for j in range(len(adj[i])):
            print(adj[i][j],end=" ")
        print()

def dfs(adj,visited,i,ans):
    visited[i]=True
    ans[0].append(i)
    for j in range(len(adj[i])):
        if visited[adj[i][j]]==False:
            dfs(adj,visited,adj[i][j],ans)

def main():
    V,E=map(int,input().split())
    adj=[[] for i in range(V)]
    for _ in range(E):
        u,v=map(int,input().split())
        adj[u].append(v)
    Print(adj,V)
    visited=[False]*V
    ans=[[]]
    for i in range(V):
        if visited[i]==False:
            dfs(adj,visited,i,ans)
    for val in ans[0]:
        print(val,end=" ")

if __name__=='__main__':
    main()

def Print(adj,V):
    for i in range(V):
        print(i," :",end=" ")
        for j in range(len(adj[i])):
            print(adj[i][j],end=" ")
        print()

def dfs(adj,i,parent,visited,V):
    visited[i]=True
    for j in range(len(adj[i])):
        if visited[adj[i][j]]==False:
            if dfs(adj,adj[i][j],i,visited,V)==True:
                return True
        elif parent!=adj[i][j]:
            return True
    return False

def IsCycle(adj,V):
    visited=[False]*V
    for i in range(V):
        if visited[i]==False:
            if dfs(adj,i,-1,visited,V)==True:
                return True
    return False

def main():
    V,E=map(int,input().split())
    adj=[[] for _ in range(V)]
    for _ in range(E):
        u,v=map(int,input().split())
        adj[u].append(v)
        adj[v].append(u)
    Print(adj,V)
    ans=IsCycle(adj,V)
    if ans==True:
        print('Cycle Present')
    else:
        print('Cycle Not Present')

if __name__=='__main__':
    main()
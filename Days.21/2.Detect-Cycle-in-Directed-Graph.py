
def Print(adj,V):
    for i in range(V):
        print(i," :",end=" ")
        for j in range(len(adj[i])):
            print(adj[i][j],end=" " )
        print()

def dfs(adj,i,visited,stack):
    visited[i]=True
    stack[i]=True
    for j in range(len(adj[i])):
        if visited[adj[i][j]]==False:
            if dfs(adj,adj[i][j],visited,stack)==True:
                return True
        elif stack[adj[i][j]]==True:
            return True
    stack[i]=False
    return False

def IsCycle(adj,V):
    visited=[False]*V
    stack=[False]*V
    for i in range(V):
        if visited[i]==False:
            if dfs(adj,i,visited,stack)==True:
                return True
    return False

def main():
    V,E=map(int,input().split())
    adj=[[] for i in range(V)]
    for _ in range(E):
        u,v=map(int,input().split())
        adj[u].append(v)
    Print(adj,V)
    ans=IsCycle(adj,V)
    if ans==True:
        print('Cycle Present')
    else:
        print('Cycle Not Present')

if __name__=='__main__':
    main()
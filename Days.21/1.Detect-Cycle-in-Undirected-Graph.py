#Detect Cycle in an undirected graph

def main():
    def DFS(i,par,V,visited,adj):
        visited[i]=par
        for j in range(len(adj[i])):
            if visited[adj[i][j]]==-1:
                b=DFS(adj[i][j],i,V,visited,adj)
                if b==True:
                    return True
            elif visited[i]!=adj[i][j]:
                return True
        return False
    V,E=map(int,input().strip().split())
    adj=[[] for _ in range(V)]
    for _ in range(E):
        u,v=map(int,input().strip().split())
        adj[u].append(v)
        adj[v].append(u)
    for i in range(V):
        print(i,end=": ")
        for j in range(len(adj[i])):
            print(adj[i][j],end=" ")
        print()
    
    flag=False
    visited=[-1 for _ in range(V)]
    for i in range(V):
        if visited[i]==-1:
            if DFS(i,i,V,visited,adj)==True:
                flag=True
                break
            
    if flag==True:
        print('Cycle Present')
    else:
        print('Cycle Not Present')





main()
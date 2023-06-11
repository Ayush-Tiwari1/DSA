#Euler Graph:
#Euler Path(Visit Edges exactly once) + start vertex==end vertex

#Shri Krishna

def dfs(i,visited,adj):
    visited[i]=True
    for j in range(len(adj[i])):
        if visited[adj[i][j]]==False:
            dfs(adj[i][j],visited,adj)

def IsEulerGraph(V,adj):
    visited=[False for i in range(V)]
    degree=[0 for i in range(V)]
    for i in range(V):
        for j in range(len(adj[i])):
            degree[adj[i][j]]+=1
    for i in range(V):
        if degree[i]>0:
            dfs(i,visited,adj)
            break
    #Connectivity Check
    for i in range(V):
        if visited[i]==False and degree[i]>0:
            return 0
    #Degree Check
    count=0
    for i in range(V):
        if degree[i]%2!=0:
            count+=1
    if count==0:
        return 1
    elif count==2:
        return 2
    return 0
    
def main():
    V,E=map(int,input().split())
    adj=[[] for i in range(V)]
    for i in range(E):
        u,v=map(int,input().split())
        adj[u].append(v)
        adj[v].append(u)
    ans=IsEulerGraph(V,adj)
    # 0---> Not Euler Graph
    # 1---> Euler Graph
    # 2---> Semi-Eulerian Graph
    if ans==1:
        print('Euler Graph')
    elif ans==2:
        print('Semi-Eulerian Graph')
    else:
        print('Not Euler Graph')

main()
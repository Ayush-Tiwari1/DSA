#Euler Circuit in Directed Graph
'''
5 6
1 0
2 1
0 2
0 3
4 0
3 4
Output: Euler Graph
'''


def dfs(i,visited,adj):
    visited[i]=True
    for j in range(len(adj[i])):
        if visited[adj[i][j]]==False:
            dfs(adj[i][j],visited,adj)

def ReverseEdges(V,adj):
    adjlist=[[] for i in range(V)]
    for i in range(V):
        for j in range(len(adj[i])):
            adjlist[adj[i][j]].append(i)
    return adjlist

def KosarajuAlgorithm(V,indegree,outdegree,adj):
    startIndx=0
    for i in range(V):
        if outdegree[i]>0:
            startIndx=i
            break
    visited=[False for i in range(V)]
    # 1. dfs check
    dfs(startIndx,visited,adj)
    for i in range(V):
        if visited[i]==False and adj[i]:
            return False
    
    for i in range(V):
        visited[i]=False
    #2. Reverse the Edges
    adjlist=ReverseEdges(V,adj)
    
    #3. Check again for startIndx with reversed Edges
    dfs(startIndx,visited,adjlist)
    for i in range(V):
        if visited[i]==False and adjlist[i]:
            return False
    return True
    
    
def EulerCircuit(V,E,adj):
    indegree=[0 for i in range(V)]
    outdegree=[0 for i in range(V)]
    for i in range(V):
        for j in range(len(adj[i])):
            outdegree[i]+=1
            indegree[adj[i][j]]+=1
    
    #1. Connectivity Check using Kosaraju's Algorithm
    ans=KosarajuAlgorithm(V,indegree,outdegree,adj)
    if ans==False:
        return False
    
    #2. Indegree==Outdegree for each vertex
    for i in range(V):
        if indegree[i]!=outdegree[i]:
            return False
    return True

def main():
    V,E=map(int,input().split())
    adj=[[] for i in range(V)]
    for i in range(E):
        u,v=map(int,input().split())
        adj[u].append(v)
    ans=EulerCircuit(V,E,adj)
    if ans==True:
        print('Euler Graph')
    else:
        print('Not Euler Graph')

main()
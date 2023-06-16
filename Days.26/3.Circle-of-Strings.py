#Circle of Strings
#Prerequisite: Euler Circuit for Directed Graph

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
    

def Kosaraju(V,indegree,outdegree,adj):
    startindx=0
    for i in range(V):
        if outdegree[i]>0:
            startindx=i
            break
    
    visited=[False for i in range(V)]
    #1. Check Dfs
    dfs(startindx,visited,adj)
    for i in range(V):
        if visited[i]==False and adj[i]:
            return False
    
    #2. Reverse the Edges
    adjlist=ReverseEdges(V,adj)
    
    for i in range(V):
        visited[i]=False
    
    #3. Check Dfs
    dfs(startindx,visited,adjlist)
    for i in range(V):
        if visited[i]==False and adjlist[i]:
            return False
    
    return True
    

def EulerCircuit(V,adj):
    
    indegree=[0 for i in range(V)]
    outdegree=[0 for i in range(V)]
    for i in range(V):
        for j in range(len(adj[i])):
            indegree[adj[i][j]]+=1
            outdegree[i]+=1
    
    #1. Connectivity Check using Kosaraju's Algorithm
    ans=Kosaraju(V,indegree,outdegree,adj)
    if ans==False:
        return False
        
    #2. Indegree==Outdegree for all vertices
    for i in range(V):
        if indegree[i]!=outdegree[i]:
            return False
    return True
    

def CircleofStrings(N,A):
    adj=[[] for i in range(26)]
    for i in range(N):
        word=A[i]
        u=ord(word[0])-ord('a')
        v=ord(word[len(word)-1])-ord('a')
        adj[u].append(v)
    
    ans=EulerCircuit(26,adj)
    return ans

def main():
    N=int(input())
    A=input().split()
    ans=CircleofStrings(N,A)
    if ans==True:
        print('Circle of Strings Possible')
    else:
        print('Circle of Strings Not Possible')


main()
#Minimum s-t cut in a flow network
#Prerequisite: Edmond-Karp's Algorithm
'''
5
0 2 0 0 0
0 0 2 3 0
0 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 4

Output: [2,4]

'''
from queue import Queue

def bfs(s,t,n,capacity,parent):
    for i in range(n):
        parent[i]=-1
    q=Queue()
    maxi=2**63
    q.put([s,maxi])
    while q.empty()==False:
        i,flow=q.get()
        if i==t:
            return flow
        for j in range(n):
            if capacity[i][j]>0 and j!=s and parent[j]==-1:
                parent[j]=i
                q.put([j,min(flow,capacity[i][j])])
    return 0
 
def dfs(i,n,visited,capacity):
    visited[i]=True
    for j in range(n):
        if capacity[i][j]>0 and visited[j]==False:
            dfs(j,n,visited,capacity)

def EdmondKarp(s,t,n,A):
    capacity=[[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            capacity[i][j]=A[i][j]
    
    maxi=2**63
    parent=[-1 for i in range(n)]
    while True:
        flow=bfs(s,t,n,capacity,parent)
        if flow==0:
            break
        v=t
        while v!=s:
            u=parent[v]
            capacity[u][v]-=flow
            capacity[v][u]+=flow
            v=u
    visited=[False for i in range(n)]
    dfs(s,n,visited,capacity)
    return visited
    

def MinimumSTCut(s,t,n,A):
    visited=EdmondKarp(s,t,n,A)
    pairs=[]
    for i in range(n):
        if visited[i]==True:
            for j in range(n):
                if visited[j]==False and A[i][j]>0:
                    pairs.append([i,j])
    
    if len(pairs)==0:
        return [-1]
    return pairs

def main():
    n=int(input())
    A=[]
    for i in range(n):
        A.append(list(map(int,input().split())))
    s,t=map(int,input().split())
    ans=MinimumSTCut(s,t,n,A)
    for cut in ans:
        print(cut)


main()
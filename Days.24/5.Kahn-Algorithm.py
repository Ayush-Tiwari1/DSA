#Topographical Sort using BFS
from queue import Queue

def KahnAlgorithm(V,adj):
    q=Queue()
    indegree=[0 for i in range(V)]
    for i in range(V):
        for j in range(len(adj[i])):
            indegree[adj[i][j]]+=1
    
    for i in range(V):
        if indegree[i]==0:
            q.put(i)
    topo=[]
    while q.empty()==False:
        u=q.get()
        topo.append(u)
        for v in adj[u]:
            indegree[v]-=1
            if indegree[v]==0:
                q.put(v)
    return topo
    

def main():
    V,E=map(int,input().split())
    adj=[[] for i in range(V)]
    for i in range(E):
        u,v=map(int,input().split())
        adj[u].append(v)
    topo=KahnAlgorithm(V,adj)
    for t in topo:
        print(t,end=" ")


main()



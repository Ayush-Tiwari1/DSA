#DAG + Order Element-----> Topographical Sort
from queue import Queue

def LongestPath(src,V,adj):

    #Topographical Sort using Kahn's Algorithm
    #Shri Krishna
    topo=[]
    indegree=[0 for i in range(V)]
    for i in range(V):
        for j in range(len(adj[i])):
            indegree[adj[i][j][0]]+=1
    q=Queue()
    for i in range(V):
        if indegree[i]==0:
            q.put(i)
    # visited=[False for i in range(V)]
    while q.empty()==False:
        i=q.get()
        topo.append(i)
        for j in range(len(adj[i])):
            if indegree[adj[i][j][0]]>0:
                indegree[adj[i][j][0]]-=1
                if indegree[adj[i][j][0]]==0:
                    q.put(adj[i][j][0])
    mini=-2**63
    distance=[mini for i in range(V)]
    distance[src]=0

    for i in topo:
        if distance[i]!=mini:
            for j in range(len(adj[i])):
                distance[adj[i][j][0]]=max(distance[adj[i][j][0]],distance[i]+adj[i][j][1])

    return distance

def main():
    V,E=map(int,input().split())
    adj=[[] for i in range(V)]
    for i in range(E):
        u,v,wt=map(int,input().split())
        adj[u].append([v,wt])
    src=int(input())
    distance=LongestPath(src,V,adj)
    for d in distance:
        print(d,end=" ")

main()




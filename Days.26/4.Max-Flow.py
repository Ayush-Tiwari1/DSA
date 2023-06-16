#Max Flow 
#Edmond's Karp Algorithm
#O(V*E^2)
from queue import Queue

def BFS(s,t,V,parent,adj,capacity):
    for i in range(V):
        parent[i]=-1
    q=Queue()
    maxi=2**63
    q.put([s,maxi])
    flow=maxi
    while q.empty()==False:
        u,flow=q.get()
        if u==t:
            return flow
        for v in adj[u]:
            if v!=s and parent[v]==-1 and capacity[u][v]>0:
                parent[v]=u
                q.put([v,min(flow,capacity[u][v])])
    return 0


def MaxFlow(V,E,Edges):
    s=0
    t=V-1
    adj=[[] for i in range(V)]
    capacity=[[0 for i in range(V)] for i in range(V)]
    for i in range(E):
        u,v,flow=Edges[i]
        u-=1
        v-=1
        adj[u].append(v)
        adj[v].append(u)
        capacity[u][v]+=flow
        capacity[v][u]+=flow
    
    maxflow=[0]
    parent=[-1 for i in range(V)]    
    while True:
        flow=BFS(s,t,V,parent,adj,capacity)
        if flow==0:
            break
        maxflow[0]+=flow
        v=t
        while v!=s:
            u=parent[v]
            capacity[u][v]-=flow
            capacity[v][u]+=flow
            v=u
            
    return maxflow[0]

def main():
    V,E=map(int,input().split())
    Edges=[]
    for i in range(E):
        u,v,flow=map(int,input().split())
        Edges.append([u,v,flow])
    ans=MaxFlow(V,E,Edges)
    print(ans)



main()
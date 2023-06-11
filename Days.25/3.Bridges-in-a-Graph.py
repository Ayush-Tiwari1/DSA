#Bridges in a Graph using Tarjan's Algorithm
'''
5 5
0 1
1 2
0 2
0 3
3 4
Bridges: [3,4], [0,3]
'''
def dfs(u,time,disc,low,parent,bridges,adj):
    disc[u]=low[u]=time[0]
    time[0]+=1
    for v in adj[u]:
        if disc[v]==-1:
            parent[v]=u
            dfs(v,time,disc,low,parent,bridges,adj)
            low[u]=min(low[u],low[v])
            if low[v]>disc[u]:
                bridges.append([u,v])
        elif parent[u]!=v:
            low[u]=min(low[u],disc[v])

def Bridges(V,adj):
    disc=[-1 for i in range(V)]
    low=[-1 for i in range(V)]
    parent=[-1 for i in range(V)]
    time=[0]
    bridges=[]
    for i in range(V):
        if disc[i]==-1:
            dfs(i,time,disc,low,parent,bridges,adj)
    if len(bridges)==0:
        return [-1,-1]
    return bridges
    

def main():
    V,E=map(int,input().split())
    adj=[[] for i in range(V)]
    for i in range(E):
        u,v=map(int,input().split())
        adj[u].append(v)
        adj[v].append(u)
    bridges=Bridges(V,adj)
    for br in bridges:
        print(br)

main()
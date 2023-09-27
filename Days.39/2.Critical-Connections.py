# Critical Connections in a Network ---> Bridges in a Network

def dfs(u,time,low,disc,parent,bridges,adj):
    low[u]=disc[u]=time[0]
    time[0]+=1
    for v in adj[u]:
        if disc[v]==-1:
            parent[v]=u
            dfs(v,time,low,disc,parent,bridges,adj)
            # Backtracking
            low[u]=min(low[u],low[v])
            if low[v]>disc[u]:
                bridges.append([u,v])
        # Back-Edge
        elif parent[u]!=v:
            low[u]=min(low[u],disc[v])


def CriticalConnections(V,connections):
    adj=[[] for i in range(V)]
    for u,v in connections:
        adj[u].append(v)
        adj[v].append(u)
    low=[-1 for i in range(V)]
    disc=[-1 for i in range(V)]
    parent=[-1 for i in range(V)]
    time=[0]
    bridges=[]
    dfs(0,time,low,disc,parent,bridges,adj)
    return bridges


def main():
    # n ---> Servers
    # e ---> Edges
    n,e=map(int,input().split())
    connections=[]
    for i in range(e):
        u,v=map(int,input().split())
        connections.append([u,v])
    bridges=CriticalConnections(n,connections)
    print('Bridges:')
    for bridge in bridges:
        print(bridge)

if __name__=='__main__':
    main()
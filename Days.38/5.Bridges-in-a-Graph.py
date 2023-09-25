# Bridges in a Graph -----> Those Edges whose removal convert
#                           graph into 2 or more components


def dfs(u,V,time,low,disc,parent,bridges,adj):
    low[u]=disc[u]=time[0]
    time[0]+=1
    for v in adj[u]:
        if disc[v]==-1:
            parent[v]=u
            dfs(v,V,time,low,disc,parent,bridges,adj)
            # Backtracking
            low[u]=min(low[u],low[v])
            if low[v]>disc[u]:
                bridges.append([u,v])
        # Back-Edge
        elif parent[u]!=v:
            low[u]=min(low[u],disc[v])
    



def Bridges(V,adj):
    low=[-1 for i in range(V)]
    disc=[-1 for i in range(V)]
    parent=[-1 for i in range(V)]
    bridges=[]
    time=[0]
    # For Disconnected Graph
    for i in range(V):
        if disc[i]==-1:
            dfs(i,V,time,low,disc,parent,bridges,adj)
    if len(bridges)==0:
        return [-1]
    return bridges



def main():
    V,E=map(int,input().split())
    adj=[[] for i in range(V)]
    for i in range(E):
        u,v=map(int,input().split())
        adj[u].append(v)
        adj[v].append(u)
    bridges=Bridges(V,adj)
    print('Bridges in a Graph:')
    for bridge in bridges:
        print(bridge)



if __name__=='__main__':
    main()
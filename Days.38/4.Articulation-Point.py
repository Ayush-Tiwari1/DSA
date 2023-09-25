# Articulation Point ---> Those vertices whose removal convert
#                         graph into 2 or more components.


def dfs(u,V,time,low,disc,parent,AP,adj):
    low[u]=disc[u]=time[0]
    time[0]+=1
    child=0
    for v in adj[u]:
        if disc[v]==-1:
            child+=1
            parent[v]=u
            dfs(v,V,time,low,disc,parent,AP,adj)
            # Backtracking
            low[u]=min(low[u],low[v])
            # Non-root Node condition
            if parent[u]!=-1 and low[v]>=disc[u]:
                AP[u]=True
        # Back-Edge
        elif parent[u]!=v:
            low[u]=min(low[u],disc[v])
    
    # Root Node condition
    if parent[u]==-1 and child>1:
        AP[u]=True


def ArticulationPoint(V,adj):
    low=[-1 for i in range(V)]
    disc=[-1 for i in range(V)]
    parent=[-1 for i in range(V)]
    AP=[False for i in range(V)]
    time=[0]
    dfs(0,V,time,low,disc,parent,AP,adj)
    ans=[]
    for i in range(V):
        if AP[i]==True:
            ans.append(i)
    if len(ans)==0:
        return [-1]
    return ans


def main():
    V,E=map(int,input().split())
    adj=[[] for i in range(V)]
    for i in range(E):
        u,v=map(int,input().split())
        adj[u].append(v)
        adj[v].append(u)
    AP=ArticulationPoint(V,adj)
    print('Articulation Points:')
    for ap in AP:
        print(ap)



if __name__=='__main__':
    main()


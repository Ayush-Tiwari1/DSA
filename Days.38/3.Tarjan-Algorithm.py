# Tarjan's Algorithm ----> Strongly Connected Component
# Single Traversal Algorithm

def dfs(u,V,time,low,disc,Instack,stack,sccs,adj):
    low[u]=disc[u]=time[0]
    time[0]+=1
    stack.append(u)
    Instack[u]=True
    for v in adj[u]:
        if disc[v]==-1:
            dfs(v,V,time,low,disc,Instack,stack,sccs,adj)
            low[u]=min(low[u],low[v])
        elif Instack[v]==True:
            low[u]=min(low[u],disc[v])
    
    if low[u]==disc[u]:
        scc=[]
        val=-1
        while val!=u:
            val=stack.pop()
            scc.append(val)
            Instack[val]=False
        sccs.append(scc)
    


def TarjanAlgorithm(V,adj):
    low=[-1 for i in range(V)]
    disc=[-1 for i in range(V)]
    Instack=[False for i in range(V)]
    stack=[]
    sccs=[]
    time=[0]
    for i in range(V):
        if disc[i]==-1:
            dfs(i,V,time,low,disc,Instack,stack,sccs,adj)
    return sccs


def main():
    V,E=map(int,input().split())
    adj=[[] for i in range(V)]
    for i in range(E):
        u,v=map(int,input().split())
        adj[u].append(v)
    sccs=TarjanAlgorithm(V,adj)
    print('Strongly Connected Components:')
    for scc in sccs:
        print(scc)



if __name__=='__main__':
    main()
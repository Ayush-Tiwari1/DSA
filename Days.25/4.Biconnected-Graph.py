#Biconnected Graph
#1. Graph must be Connected
#2. No Articulation Point in the Graph


'''
5 6
1 0 
0 2 
2 1 
0 3 
3 4 
2 4

Output: Biconnected Graph
'''


def dfs(u,time,disc,low,parent,AP,adj):
    disc[u]=low[u]=time[0]
    time[0]+=1
    count=0
    for v in adj[u]:
        if disc[v]==-1:
            count+=1
            parent[v]=u
            dfs(v,time,disc,low,parent,AP,adj)
            low[u]=min(low[u],low[v])
            if parent[u]==-1 and count>1:
                AP[u]=True
            if parent[u]!=-1 and low[v]>=disc[u]:
                AP[u]=True
        elif parent[u]!=v:
            low[u]=min(low[u],disc[v])
            
            

def BiconnectedGraph(V,adj):
    disc=[-1 for i in range(V)]
    low=[-1 for i in range(V)]
    parent=[-1 for i in range(V)]
    AP=[False for i in range(V)]
    time=[0]
    dfs(0,time,disc,low,parent,AP,adj)
    for i in range(V):
        if disc[i]==-1:
            return False
    for i in range(V):
        if AP[i]==True:
            return False
    return True

def main():
    V,E=map(int,input().split())
    adj=[[] for i in range(V)]
    for i in range(E):
        u,v=map(int,input().split())
        adj[u].append(v)
        adj[v].append(u)
    ans=BiconnectedGraph(V,adj)
    if ans==True:
        print('Biconnected Graph')
    else:
        print('Not Biconnected Graph')
    

main()
#Articulation Point
'''
5 5
0 1
1 4
4 2
2 3
4 3
AP: 1 4
'''
def dfs(u,time,disc,low,parent,AP,adj):
    disc[u]=time[0]
    low[u]=time[0]
    #For Counting Children
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

def ArticulationPoint(V,adj):
    disc=[-1 for i in range(V)]
    low=[-1 for i in range(V)]
    parent=[-1 for i in range(V)]
    AP=[False for i in range(V)]
    time=[0]
    for i in range(V):
        if disc[i]==-1:
            dfs(i,time,disc,low,parent,AP,adj)
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
    for ap in AP:
        print(ap,end=" ")


main()
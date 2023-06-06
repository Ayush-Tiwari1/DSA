#Shortest Path in Directed Acyclic Graph

def main():
    def dfs(i,visited,topo,adj):
        visited[i]=True
        for j in range(len(adj[i])):
            if visited[adj[i][j][0]]==False:
                dfs(adj[i][j][0],visited,topo,adj)
        
        topo.append(i)
    
    def ShortestPath(src,V,adj):
        topo=[]
        #Topographical sort
        visited=[False for i in range(V)]
        for i in range(V):
            if visited[i]==False:
                dfs(i,visited,topo,adj)
        topo.reverse()
        print(topo)
        maxi=2**63
        distance=[maxi for i in range(V)]
        distance[src]=0
        for u in topo:
            for j in adj[u]:
                v,wt=j
                if distance[u]!=maxi and distance[u]+wt<distance[v]:
                    distance[v]=distance[u]+wt
        return distance
        
    
    V,E=map(int,input().split())
    adj=[[] for i in range(V)]
    for i in range(E):
        u,v,wt=map(int,input().split())
        adj[u].append([v,wt])
    src=int(input())
    distances=ShortestPath(src,V,adj)
    for d in distances:
        print(d,end=" ")

main()
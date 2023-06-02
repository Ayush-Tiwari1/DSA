#Strongly Connected Components-----> Kosaraju's Algorithm
#1. Topographical Sort
#2. Reverse the edges of adjacency list
#3. Find dfs from Topographical sort, count and store Strongly Connected Components



def main():
    
    def TopographicalSort(i,V,topo,visited,adj):
        visited[i]=True
        for j in range(len(adj[i])):
            if visited[adj[i][j]]==False:
                TopographicalSort(adj[i][j],V,topo,visited,adj)
        topo.append(i)
    
    def dfs(i,V,temp,visited,adjlist):
        visited[i]=True
        temp.append(i)
        for j in range(len(adjlist[i])):
            if visited[adjlist[i][j]]==False:
                dfs(adjlist[i][j],V,temp,visited,adjlist)
    
    def KosarajuAlgorithm(V,adj):
        topo=[]
        visited=[False for i in range(V)]
        #1st step: topographical sort
        for i in range(V):
            if visited[i]==False:
               TopographicalSort(i,V,topo,visited,adj)
        topo.reverse()
        
        #2nd Step: Reverse the Edges1
        adjlist=[[] for i in range(V)]
        for i in range(V):
            for j in range(len(adj[i])):
                adjlist[adj[i][j]].append(i)
        
        #3rd Step: dfs using topographical sort to the reverse edge adjacency list
        ans=[]
        count=0
        for i in range(V):
            visited[i]=False
        for i in range(len(topo)):
            if visited[topo[i]]==False:
                count+=1
                temp=[]
                dfs(topo[i],V,temp,visited,adjlist)
                ans.append(temp)
        return [ans,count]
    
    V,E=map(int,input().strip().split())
    adj=[[] for i in range(V)]
    for i in range(V):
        u,v=map(int,input().strip().split())
        adj[u].append(v)
    ans,count=KosarajuAlgorithm(V,adj)
    for val in ans:
        print(val)
    print('Total SCC:',count)

main()
#Strongly Connected Components--------> Tarjan's Algorithm
#O(V+E) Time complexity
#Single Traversal Algorithm

def main():
    
    def dfs(u,time,disc,low,Instack,stack,adj,ans):
        disc[u]=low[u]=time[0]
        Instack[u]=True
        stack.append(u)
        time[0]+=1
        for v in adj[u]:
            if disc[v]==-1:
                dfs(v,time,disc,low,Instack,stack,adj,ans)
                low[u]=min(low[u],low[v])
            elif Instack[v]==True: #BackEdge
                low[u]=min(low[u],disc[v])
        
        #Head Node
        if low[u]==disc[u]:
            temp=[]
            val=-1
            while val!=u:
                val=stack.pop()
                temp.append(val)
                Instack[val]=False
            temp.sort()
            ans.append(temp)
        
    
    def TarjanAlgorithm(V,adj):
        disc=[-1 for i in range(V)]
        low=[-1 for i in range(V)]
        Instack=[False for i in range(V)]
        stack=[]
        time=[0]
        ans=[]
        for i in range(V):
            if disc[i]==-1:
                dfs(i,time,disc,low,Instack,stack,adj,ans)
        return ans
    
    V,E=map(int,input().strip().split())
    adj=[[] for i in range(V)]
    for i in range(E):
        u,v=map(int,input().strip().split())
        adj[u].append(v)
    ans=TarjanAlgorithm(V,adj)
    for scc in ans:
        print(scc)
    print('Total SCC:',len(ans))


main()
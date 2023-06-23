# Travelling Salesman Problem using DP + Bitmasking
# NP hard Problem whose solution cannot be polynomial 

def TSP(n,graph):
    dp=[[None]*(1<<n) for i in range(n)]
    maxi=2**63
    def tsp(curr_node,mask):
        if mask== (1<<n)-1:
            return graph[curr_node][0]
        if dp[curr_node][mask] is not None:
            return dp[curr_node][mask]
        
        ans=maxi
        
        for i in range(n):
            if (1<<i) & mask==0:
                ans=min(ans,graph[curr_node][i]+tsp(i,mask| (1<<i)))
        
        dp[curr_node][mask]=ans
        return dp[curr_node][mask]
    
    return tsp(0,1)

def main():
    n=int(input())
    graph=[]
    for i in range(n):
        graph.append(list(map(int,input().split())))
    
    min_distance=TSP(n,graph)
    print(min_distance)

main()
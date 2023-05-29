#Minimum Spanning Tree---> Prim's Algorithm
#Prim's Algorithm ---> BFS + PriorityQueue
from queue import PriorityQueue

def PrimsAlgorithm(adj,V):
    pq=PriorityQueue()
    pq.put([0,0,-1])
    #[dist,node,parent]
    sum=0
    visited=[False]*V
    #BFS---> rm*wa* ---> remove mark* work add*
    while pq.qsize()>0:
        temp=pq.get()
        d=temp[0]
        i=temp[1]
        # par=temp[2]
        if visited[i]==False:
            visited[i]=True
            sum+=d
            for j in range(len(adj[i])):
                if visited[adj[i][j][0]]==False:
                    pq.put([adj[i][j][1],adj[i][j][0],i])

    return sum

def main():
    V,E=map(int,input().split())
    adj=[[] for i in range(V)]
    for _ in range(E):
        u,v,wt=map(int,input().split())
        adj[u].append([v,wt])
        adj[v].append([u,wt])
    sum=PrimsAlgorithm(adj,V)
    print(sum)

if __name__=='__main__':
    main()
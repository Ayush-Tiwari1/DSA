#Dijkstra-Algorithm----> Shortest Path from the Source to all other nodes.
#Not able to detect Negative-Edge Weight Cycle
from queue import PriorityQueue

def DijkstraAlgorithm(adj,V,S):
    dist=[-1]*V
    pq=PriorityQueue()
    pq.put([0,S])
    size=1
    #BFS ----> rm*wa*  ----> remove mark* work add*
    while size>0:
        temp=pq.get()
        size-=1
        d=temp[0]
        i=temp[1]
        if dist[i]==-1:
            dist[i]=d
            for j in range(len(adj[i])):
                if dist[adj[i][j][0]]==-1:
                    pq.put([d+adj[i][j][1],adj[i][j][0]])
                    size+=1
    return dist

def main():
    V,E=map(int,input().strip().split())
    adj=[[] for _ in range(V)]
    for _ in range(E):
        u,v,dist=map(int,input().strip().split())
        adj[u].append([v,dist])
        adj[v].append([u,dist])
    S=int(input())
    dist=DijkstraAlgorithm(adj,V,S)
    for d in dist:
        print(d,end=" ")


if __name__=='__main__':
    main()
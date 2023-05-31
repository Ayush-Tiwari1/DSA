#Dijkstra's Algorithm
from queue import PriorityQueue
def main():
    def DijkstraAlgorithm(src,V,adj,distance):
        #BFS + Priority Queue
        #rm*wa*
        pq=PriorityQueue()
        pq.put([0,src])
        while pq.empty() == False:
            dist,sc=pq.get()
            if distance[sc]==-1:
                print(dist,sc)
                distance[sc]=dist
                for j in range(len(adj[sc])):
                    if distance[adj[sc][j][0]]==-1:
                        pq.put([dist+adj[sc][j][1],adj[sc][j][0]])
        
        
    V,E=map(int,input().strip().split())
    adj=[[] for i in range(V)]
    for i in range(E):
        u,v,dist=map(int,input().strip().split())
        adj[u].append([v,dist])
        adj[v].append([u,dist])
    src=int(input())
    distance=[-1 for i in range(V)]
    DijkstraAlgorithm(src,V,adj,distance)
    print(distance)


main()
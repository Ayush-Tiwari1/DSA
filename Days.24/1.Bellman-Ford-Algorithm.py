#Bellman Ford Algorithm
#It can detect Negative Edge Weight Cycle

def main():
    def BellmanFord(src,V,edges):
        maxi=2**63
        distance=[maxi for i in range(V)]
        distance[src]=0
        for i in range(V-1):
            for j in edges:
                u,v,wt=j
                if distance[u]!=maxi and distance[u]+wt<distance[v]:
                    distance[v]=distance[u]+wt
        for j in edges:
            u,v,wt=j
            if distance[u]!=maxi and distance[u]+wt<distance[v]:
                return [-1]
        return distance
            
        
    V,E=map(int,input().strip().split())
    edges=[]
    for i in range(E):
        u,v,wt=map(int,input().strip().split())
        edges.append([u,v,wt])
    src=int(input())
    distance=BellmanFord(src,V,edges)
    if distance[0]==-1:
        print('Negative Edge Weight Cycle Present')
    else:
        for i in range(len(distance)):
            print(i,distance[i])
    

main()
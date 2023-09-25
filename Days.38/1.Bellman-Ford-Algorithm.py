# Bellman Ford Algorithm
# It can detect Negative Edge Weight Cycle


def BellmanFord(V,src,Edges):
    maxi=int(1e8)
    dist=[maxi for i in range(V)]
    dist[src]=0
    for i in range(V-1):
        flag=False
        for u,v,wt in Edges:
            if dist[u]!=maxi and dist[u]+wt<dist[v]:
                flag=True
                dist[v]=dist[u]+wt
        if flag==False:
            return dist
    
    # checking Negative Edge Weight Cycle
    for u,v,wt in Edges:
        if dist[u]!=maxi and dist[u]+wt<dist[v]:
            return []
    return dist
            




def main():
    V,E=map(int,input().split())
    Edges=[]
    for i in range(E):
        Edges.append(list(map(int,input().split())))
    src=int(input())
    distance=BellmanFord(V,src,Edges)
    if len(distance)==0:
        print('Graph Contains Negative Edge Weight Cycle')
    else:
        for dist in distance:
            print(dist,end=" ")
    print()



if __name__=='__main__':
    main()
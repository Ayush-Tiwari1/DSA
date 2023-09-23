# 0-1 BFS
# Minimum Number of Edges to reverse for reaching destination from source
from collections import deque

def _01BFS(src,dest,V,adj):
    
    visited=[False for i in range(V)]
    for u in range(V):
        for v,wt in adj[u]:
            if wt==0:
                adj[v].append([u,1])
    # for u in range(V):
    #     print(u,":",sep="",end=" ")
    #     for v in adj[u]:
    #         print(v,end=" ")
    #     print()
    dq=deque()
    dq.append([src,0])
    visited[src]=True
    while dq:
        u,dist=dq.popleft()
        # print(u,dist)
        if u==dest:
            return dist
        for v,wt in adj[u]:
            if visited[v]==False:
                visited[v]=True
                if wt==0:
                    dq.appendleft([v,dist])
                else:
                    dq.append([v,dist+wt])
                    
    return -1


def main():
    V,E=map(int,input().split())
    adj=[[] for i in range(V)]
    for i in range(E):
        u,v=map(int,input().split())
        adj[u].append([v,0])
    src,dest=map(int,input().split())
    ans=_01BFS(src,dest,V,adj)
    print(ans)



if __name__=='__main__':
    main()
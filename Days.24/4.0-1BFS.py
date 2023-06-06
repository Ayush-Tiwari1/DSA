#0-1 BFS
'''
7 7
0 1
5 1
2 1
2 3
6 3
6 4
4 5
0 6
'''
from collections import deque

def _01BFS(src,dst,V,adj):
    print('(Vertex,Sum)')
    for i in range(V):
        for j in range(len(adj[i])):
            adj[adj[i][j][0]].append([i,1])

    dq=deque()
    dq.append([src,0])
    visited=[False for i in range(V)]
    #rm*wa*
    while dq:
        i,wt=dq.popleft()
        if visited[i]==False:
            print(i,wt)
            visited[i]=True
            if i==dst:
                print(wt)
                return wt
            for j in range(len(adj[i])):
                if adj[i][j][1]==0:
                    dq.appendleft([adj[i][j][0],wt])
                else:
                    dq.append([adj[i][j][0],wt+adj[i][j][1]])
    
    

def main():
    V,E=map(int,input().split())
    adj=[[] for i in range(V)]
    for i in range(E):
        u,v=map(int,input().split())
        adj[u].append([v,0])
    src,dst=map(int,input().split())
    ans=_01BFS(src,dst,V,adj)
    print('Minimum Number of Edges to be Reverse:',ans)


main()
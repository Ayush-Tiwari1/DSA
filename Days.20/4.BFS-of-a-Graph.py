from typing import List
from queue import Queue
def Print(adj:List[List[int]],V:int):
    for i in range(V):
        print(i,":",end=" ")
        for j in range(len(adj[i])):
            print(adj[i][j],end=" ")
        print()

def BFS(adj:List[List[int]],V:int)->List[int]:
    ans=[]
    q=Queue()
    q.put(0)
    visited=[False]*V
    visited[0]=True
    while q.qsize()>0:
        i=q.get()
        ans.append(i)
        for j in range(len(adj[i])):
            if visited[adj[i][j]]==False:
                q.put(adj[i][j])
                visited[adj[i][j]]=True
    return ans

def main():
    V,E=map(int,input().split())
    adj=[[] for i in range(V)]
    for _ in range(E):
        u,v=map(int,input().split())
        adj[u].append(v)
    Print(adj,V)
    ans=BFS(adj,V)
    for val in ans:
        print(val,end=" ")

if __name__=='__main__':
    main()
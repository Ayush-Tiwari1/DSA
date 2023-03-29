
'''
BFS Funda:    rm*wa*---> remove mark* work add*
'''
from queue import Queue
def Print(adj,V):
    for i in range(V):
        print(i," :",end=" ")
        for j in range(len(adj[i])):
            print(adj[i][j],end=" ")
        print()

def IsGraphBipartite(adj,V):
    q=Queue()
    visited=[-1]*V
    for indx in range(V):
        if visited[indx]==-1:
            q.put([indx,0])
            while q.qsize()>0:
                temp=q.get()
                i=temp[0]
                level=temp[1]
                if visited[i]==-1:
                    visited[i]=level
                    for j in range(len(adj[i])):
                        if visited[adj[i][j]]==-1:
                            q.put([adj[i][j],level+1])
                elif visited[i]!=level:
                    return False
    
    return True

def main():
    V,E=map(int,input().strip().split())
    adj=[[] for _ in range(V)]
    for i in range(E):
        u,v=map(int,input().strip().split())
        adj[u].append(v)
        adj[v].append(u)
    Print(adj,V)
    ans=IsGraphBipartite(adj,V)
    if ans==True:
        print('Graph Bipartite')
    else:
        print('Graph Not Bipartite')

if __name__=='__main__':
    main()
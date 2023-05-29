from queue import Queue

def main():
    def BFS(adj,V):
        #rm*wa*
        visited=[False for i in range(V)]
        q=Queue()
        q.put(0)
        ans=[]
        while q.empty()==False:
            u=q.get()
            if visited[u]==False:
                ans.append(u)
            visited[u]=True
            for v in range(len(adj[u])):
                if visited[adj[u][v]]==False:
                    q.put(adj[u][v])
        return ans
    V,E=map(int,input().strip().split())
    adj=[[] for i in range(V)]
    for _ in range(E):
        u,v=map(int,input().strip().split())
        adj[u].append(v)
    
    for i in range(V):
        print(i,end=":")
        for j in range(len(adj[i])):
            print(adj[i][j],end=" ")
        print()
    print('BFS:',end=" ")
    ans=BFS(adj,V)
    for val in ans:
        print(val,end=" ")
    print()

main()
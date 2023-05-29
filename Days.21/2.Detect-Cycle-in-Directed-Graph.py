#BFS
def Print(adj,V):
    for i in range(V):
        print(i," :",end=" ")
        for j in range(len(adj[i])):
            print(adj[i][j],end=" " )
        print()

def dfs(adj,i,visited,stack):
    visited[i]=True
    stack[i]=True
    for j in range(len(adj[i])):
        if visited[adj[i][j]]==False:
            if dfs(adj,adj[i][j],visited,stack)==True:
                return True
        elif stack[adj[i][j]]==True:
            return True
    stack[i]=False
    return False

def IsCycle(adj,V):
    visited=[False]*V
    stack=[False]*V
    for i in range(V):
        if visited[i]==False:
            if dfs(adj,i,visited,stack)==True:
                return True
    return False

def main():
    V,E=map(int,input().split())
    adj=[[] for i in range(V)]
    for _ in range(E):
        u,v=map(int,input().split())
        adj[u].append(v)
    Print(adj,V)
    ans=IsCycle(adj,V)
    if ans==True:
        print('Cycle Present')
    else:
        print('Cycle Not Present')

if __name__=='__main__':
    main()


#DFS
#Detect Cycle in Directed Graph

def main():
    def DFS(i,V,adj,visited,order):
        visited[i]=True
        order[i]=True
        for j in range(len(adj[i])):
            if visited[adj[i][j]]==False:
                b=DFS(adj[i][j],V,adj,visited,order)
                if b==True:
                    return True
            elif order[adj[i][j]]==True:
                return True
        order[i]=False
        return False
    V,E=map(int,input().strip().split())
    adj=[[] for _ in range(V)]
    for _ in range(E):
        u,v=map(int,input().strip().split())
        adj[u].append(v)
    for i in range(V):
        print(i,end=": ")
        for j in range(len(adj[i])):
            print(adj[i][j],end= " ")
        print()
    flag=False
    visited=[False for _ in range(V)]
    order=[False for _ in range(V)]
    for i in range(V):
        if visited[i]==False:
            b=DFS(i,V,adj,visited,order)
            if b==True:
                flag=True
                break
    
    if flag==True:
        print('Cycle Present')
    else:
        print('Cycle Not Present')




main()
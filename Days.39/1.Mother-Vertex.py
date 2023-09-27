# Mother Vertex

def dfs(u,visited,temp,adj):
    visited[u]=True
    for v in adj[u]:
        if visited[v]==False:
            dfs(v,visited,temp,adj)
    temp.append(u)


def MotherVertex(V,adj):
    visited=[False for i in range(V)]
    temp=[]
    for i in range(V):
        if visited[i]==False:
            dfs(i,visited,temp,adj)
    mother=temp[-1]
    for i in range(V):
        visited[i]=False
    temp=[]
    dfs(mother,visited,temp,adj)
    for i in range(V):
        if visited[i]==False:
            return -1
    return mother



def main():
    V,E=map(int,input().split())
    adj=[[] for i in range(V)]
    for i in range(E):
        u,v=map(int,input().split())
        adj[u].append(v)
    ans=MotherVertex(V,adj)
    print('Mother Vertex:',ans)
    



if __name__=='__main__':
    main()
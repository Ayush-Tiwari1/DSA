# Print All Hamiltonian Path and Cycles
'''
Input:
7
0 1 0 1 0 0 0
1 0 1 0 0 0 0
0 1 0 1 0 1 0
1 0 1 0 1 0 0
0 0 0 1 0 1 1
0 0 1 0 1 0 1
0 0 0 0 1 1 0

Output:
Hamiltonian Paths:
0-1-2-3-4-5-6
0-1-2-3-4-6-5
Hamiltonian Cycles:
0-1-2-5-6-4-3
0-3-4-6-5-2-1

'''
def dfs(i,count,path,visited,V,graph,hamiltonian_paths,hamiltonian_cycles):
    if count==V:
        if graph[i][0]==1:
            hamiltonian_cycles.append(path)
        else:
            hamiltonian_paths.append(path)
        return 
    visited[i]=True
    for j in range(V):
        if graph[i][j]==1 and visited[j]==False:
            dfs(j,count+1,path+'-'+str(j),visited,V,graph,hamiltonian_paths,hamiltonian_cycles)
    visited[i]=False


def main():
    V=int(input())
    graph=[]
    for i in range(V):
        graph.append(list(map(int,input().split())))
    hamiltonian_paths=[]
    hamiltonian_cycles=[]
    count=1
    path="0"
    visited=[False for i in range(V)]
    dfs(0,count,path,visited,V,graph,hamiltonian_paths,hamiltonian_cycles)
    
    print('Hamiltonian Paths:')
    for path in hamiltonian_paths:
        print(path)
    print('Hamiltonian Cycles:')
    for path in hamiltonian_cycles:
        print(path)
    

if __name__=="__main__":
    main()


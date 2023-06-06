#Cloned Graph
from queue import Queue

class Node:
    def __init__(self,val=0,neighbors=[]):
        self.val=val
        self.neighbors=neighbors

def CloneGraph(node):
    dict={}
    q=Queue()
    q.put(node)
    while q.empty()==False:
        temp=q.get()
        if temp not in dict:
            dict[temp]=Node(temp.val)
        for nb in temp.neighbors:
            if nb not in dict:
                dict[nb]=Node(nb.val)
                q.put(nb)
            dict[temp].neighbors.append(dict[nb])
            
    return dict[node]
    

def bfs(src):
    ans=[]
    q=Queue()
    visited=set()
    q.put(src)
    while q.empty()==False:
        temp=q.get()
        if temp not in visited:
            visited.add(temp)
            ans.append(temp)
            for i in temp.neighbors:
                if i not in visited:
                    q.put(i)
    return ans

def Check(src1,src2):
    b1=bfs(src1)
    b2=bfs(src2)
    for v in b1:
        print(v,v.val)
    for v in b2:
        print(v,v.val)
    return b1==b2
    
def main():
    n=int(input())
    v=[Node(i) for i in range(n)]
    for i in range(n):
        v[i].neighbors=[v[int(i)] for i in input().split()]
    ans=Check(v[0],CloneGraph(v[0]))
    print(ans)
    if ans==True:
        print('Clone Graph Successfully')
    else:
        print('Not Clone Graph')

main()
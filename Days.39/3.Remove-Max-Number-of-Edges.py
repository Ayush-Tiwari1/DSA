# Remove Max Number of Edges to Keep Graph Fully Traversable

'''
Input:
4 6
3 0 1
3 1 2
1 0 2
1 1 3
1 0 1
2 2 3
Output:
Removed Edges are: 2
'''


# Find By Path Compression
def Find(u,parent):
    if parent[u]==-1:
        return u
    parent[u]=Find(parent[u],parent)
    return parent[u]
    

# Union By Rank
def Union(x,y,rank,parent):
    if rank[x]==rank[y]:
        parent[y]=x
        rank[x]+=1
    elif rank[x]>rank[y]:
        parent[y]=x
    else:
        parent[x]=y
        

def DSU(V,Edges):
    remove=0
    alicecount=1
    bobcount=1
    aliceparent=[-1 for i in range(V)]
    alicerank=[0 for i in range(V)]
    bobparent=[-1 for i in range(V)]
    bobrank=[0 for i in range(V)]
    
    for type,u,v in Edges:
        if type==1:
            x=Find(u,aliceparent)
            y=Find(v,aliceparent)
            if x!=y:
                Union(x,y,alicerank,aliceparent)
                alicecount+=1
            else:
                remove+=1
        elif type==2:
            x=Find(u,bobparent)
            y=Find(v,bobparent)
            if x!=y:
                Union(x,y,bobrank,bobparent)
                bobcount+=1
            else:
                remove+=1
        else:
            flag=False
            x=Find(u,aliceparent)
            y=Find(v,aliceparent)
            if x!=y:
                Union(x,y,alicerank,aliceparent)
                alicecount+=1
                flag=True
            x=Find(u,bobparent)
            y=Find(v,bobparent)
            if x!=y:
                Union(x,y,bobrank,bobparent)
                bobcount+=1
                flag=True
            if flag==False:
                remove+=1
    if alicecount==V and bobcount==V:
        return remove
    return -1
            



def RemoveMaxEdges(V,Edges):
    Edges.sort(key=lambda x: x[0],reverse=True)
    return DSU(V,Edges)



def main():
    V,E=map(int,input().split())
    Edges=[]
    for i in range(E):
       Edges.append(list(map(int,input().split())))
    ans=RemoveMaxEdges(V,Edges)
    if ans==-1:
        print('Graph Cannot be Fully Traversable')
    else:
        print('Removed Edges are:',ans)





if __name__=='__main__':
    main()
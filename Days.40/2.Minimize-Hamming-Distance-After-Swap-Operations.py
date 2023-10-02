# Minimize Hamming Distance After Swap Operations

# Find by Path Compression
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


def MinimumHammingDistance(source,target,allowedSwaps):
    n=len(source)
    # Disjoint Set Union
    parent=[-1 for i in range(n)]
    rank=[0 for i in range(n)]
    for i,j in allowedSwaps:
        x=Find(i,parent)
        y=Find(j,parent)
        if x!=y:
            Union(x,y,rank,parent)
    dict={}
    # dict={val:{dictionary}}
    for i in range(n):
        par=i
        if parent[i]!=-1:
            par=Find(parent[i],parent)
        if par in dict:
            if source[i] in dict[par]:
                dict[par][source[i]]+=1
            else:
                dict[par][source[i]]=1
                
        else:
            dict[par]={source[i]:1}
    
    ans=0
    for i in range(n):
        par=i
        if parent[i]!=-1:
            par=Find(parent[i],parent)
        if target[i] in dict[par] and dict[par][target[i]]>0:
            dict[par][target[i]]-=1
        else:
            ans+=1
    
    return ans
    
    
def main():
    n=int(input())
    source=list(map(int,input().split()))
    target=list(map(int,input().split()))
    k=int(input())
    allowedSwaps=[]
    for i in range(k):
        allowedSwaps.append(list(map(int,input().split())))
    ans=MinimumHammingDistance(source,target,allowedSwaps)
    print('Minimum Hamming Distance:',ans)



if __name__=='__main__':
    main()
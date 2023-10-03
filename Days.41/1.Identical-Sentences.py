# Identical Sentences

# Find by Path Compression
def Find(u,parent):
    if parent[u]==-1:
        return u
    parent[u]=Find(parent[u],parent)
    return parent[u]

# Union by Rank
def Union(x,y,rank,parent):
    if rank[x]>rank[y]:
        parent[y]=x
    elif rank[x]<rank[y]:
        parent[x]=y
    else:
        parent[y]=x
        rank[x]+=1



def IdenticalSentences(n,m,p,word1,word2,pairs):
    if n!=m:
        return False
    StringId={}
    IdString={}
    uid=0
    for u,v in pairs:
        if u not in StringId:
            StringId[u]=uid
            IdString[uid]=u
            uid+=1
        if v not in StringId:
            StringId[v]=uid
            IdString[uid]=v
            uid+=1
    parent=[-1 for i in range(uid)]
    rank=[0 for i in range(uid)]
    for u,v in pairs:
        x=Find(StringId[u],parent)
        y=Find(StringId[v],parent)
        if x!=y:
            Union(x,y,rank,parent)
    for i in range(n):
        if word1[i]==word2[i]:
            continue
        if word1[i] not in StringId or word2[i] not in StringId:
            return False
        x=Find(StringId[word1[i]],parent)
        y=Find(StringId[word2[i]],parent)
        if x!=y:
            return False
    return True



def main():
    n=int(input())
    word1=list(input().split())
    m=int(input())
    word2=list(input().split())
    p=int(input())
    pairs=[]
    for i in range(p):
        pairs.append(list(input().split()))
    ans=IdenticalSentences(n,m,p,word1,word2,pairs)
    if ans==True:
        print('Sentences are Identical')
    else:
        print('Sentences are Not Identical')



if __name__=='__main__':
    main()
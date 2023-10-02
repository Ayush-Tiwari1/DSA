# Accounts Merge
'''

Input:
4 ----> n
3
John johnsmith@mail.com john_newyork@mail.com
3
John johnsmith@mail.com john00@mail.com
2
Mary mary@mail.com
2
John johnnybravo@mail.com

Output:
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']
['Mary', 'mary@mail.com']
['John', 'johnnybravo@mail.com']


'''
# Find by Path Compression
def Find(u,parent):
    if parent[u]==-1:
        return u
    parent[u]=Find(parent[u],parent)
    return parent[u]


# Union by Rank
def Union(x,y,rank,parent):
    if rank[x]==rank[y]:
        parent[y]=x
        rank[x]+=1
    elif rank[x]>rank[y]:
        parent[y]=x
    else:
        parent[x]=y



def AccountsMerge(accounts):
    EmailId={} # email --> unique id
    EmailName={} # email --> name
    IdEmail={} # unique id ---> email
    uid=0
    for account in accounts:
        name=account[0]
        for i in range(1,len(account)):
            email=account[i]
            if email not in EmailId:
                EmailId[email]=uid
                IdEmail[uid]=email
                EmailName[email]=name
                uid+=1
    n=uid
    
    
    # Disjoint Set Union
    parent=[-1 for i in range(n)]
    rank=[0 for i in range(n)]
    for account in accounts:
        for i in range(1,len(account)-1):
            u=EmailId[account[i]]
            v=EmailId[account[i+1]]
            x=Find(u,parent)
            y=Find(v,parent)
            if x!=y:
                Union(x,y,rank,parent)
    # email--> all pairs
    dict={}
    for i in range(n):
        par=i
        if parent[i]!=-1:
            par=Find(parent[i],parent)
        if par in dict:
            dict[par].append(IdEmail[i])
        else:
            dict[par]=[IdEmail[i]]
    ans=[]
    for key,value in dict.items():
        value.sort()
        lst=[]
        lst.append(EmailName[value[0]])
        lst.extend(value)
        ans.append(lst)
        
    return ans


def main():
    accounts=[]
    n=int(input())
    for i in range(n):
        k=int(input())
        accounts.append(list(input().split()))
    ans=AccountsMerge(accounts)
    for account in ans:
        print(account)




if __name__=='__main__':
    main()
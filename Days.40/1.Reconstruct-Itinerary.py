# Reconstruct Itinerary

import heapq

def dfs(out,dict,ans):
    
    while out in dict and len(dict[out])>0:
        top=dict[out][0]
        heapq.heappop(dict[out])
        dfs(top,dict,ans)
    
    ans.append(out)

def FindItinerary(n,tickets):
    indegree={}
    outdegree={}
    
    for fm,to in tickets:
        if fm in outdegree:
            outdegree[fm]+=1
        else:
            outdegree[fm]=1
        if to in indegree:
            indegree[to]+=1
        else:
            indegree[to]=1
    outcount=0
    indcount=0
    out="JFK"
    ind=""
    for indeg,icount in indegree.items():
        ocount=outdegree.get(indeg,0)
        if icount==ocount+1:
            ind=indeg
            indcount+=1
    for outdeg,ocount in outdegree.items():
        icount=indegree.get(outdeg,0)
        if ocount==icount+1:
            out=outdeg
            outcount+=1
    if indcount>1 or outcount>1:
        return []
    # dict ---> ticket: priority Queue
    dict={}
    for fm,to in tickets:
        if fm in dict:
            heapq.heappush(dict[fm],to)
        else:
            dict[fm]=[to]
    ans=[]
    dfs(out,dict,ans)
    ans.reverse()
    return ans
    

def main():
    n=int(input())
    tickets=[]
    for i in range(n):
        tickets.append(list(input().split()))
    ans=FindItinerary(n,tickets)
    for ticket in ans:
        print(ticket,end=" ---> ")




if __name__=='__main__':
    main()
# Alien Dictionary
# N ---> Total Number of Words
# K ---> Starting Alphabets of Standard Dictionary [E.g, k=4---> abcd]
# Dict---> Total Words of Alien Dictionary
# Return Order of characters if alien dictionary is sorted

from collections import deque


def AlienDictionary(N,K,dict):
    adj=[[] for i in range(K)]
    i=0
    while i<N-1:
        str1=dict[i]
        str2=dict[i+1]
        j=0
        while j<len(str1) and j<len(str2) and str1[j]==str2[j]:
            j+=1
        if j<len(str1) and j<len(str2):
            u=ord(str1[j])-ord('a')
            v=ord(str2[j])-ord('a')
            adj[u].append(v)
        i+=1
    
    # Kahn's Algorithm
    indegree=[0 for i in range(K)]
    for u in range(K):
        for v in adj[u]:
            indegree[v]+=1
    
    dq=deque()
    for i in range(K):
        if indegree[i]==0:
            dq.append(i)
    
    order=[]
    while dq:
        u=dq.popleft()
        order.append(chr(u+ord('a')))
        for v in adj[u]:
            indegree[v]-=1
            if indegree[v]==0:
                dq.append(v)
    
    return order



def main():
    N,K=map(int,input().split())
    dict=list(input().split())
    order=AlienDictionary(N,K,dict)
    for char in order:
        print(char,'-->',end= "")
    print()



if __name__=='__main__':
    main()
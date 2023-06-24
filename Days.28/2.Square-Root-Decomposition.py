#Square Root Decomposition for min values
#Time Complexity: O(q*sqrt(n)) q---> total queries, n---> Total number of elements

'''
16
2 3 -1 9 6 -2 10 4 12 -1 5 7 16 -4 8 3
3
1 13
10 15
0 7

Output:
Query:1	(1,13)	Min Value: -4
Query:2	(10,15)	Min Value: -4
Query:3	(0,7)	Min Value: -2

'''

import math 

def SquareRootDecomposition(n,arr,q,queries):
    #len---> sqrt(n)
    len=math.ceil(n**0.5)
    sqrt=[2**63 for i in range(len)]
    for i in range(n):
        sqrtindx=i//len
        sqrt[sqrtindx]=min(sqrt[sqrtindx],arr[i])
    
    #Running Queries
    for i in range(q):
        l=queries[i][0]
        r=queries[i][1]
        mini=2**63
        print('Query',i+1,sep=":",end="\t")
        print('(',l,',',r,')',sep='',end="\t")
        while l<=r:
            if l%len==0 and (l+len-1)<=r:
                mini=min(mini,sqrt[l//len])
                l+=len
            else:
                mini=min(mini,arr[l])
                l+=1
        print('Min Value:',mini)
        
    

def main():
    n=int(input())
    arr=list(map(int,input().split()))
    q=int(input())
    queries=[]
    for i in range(q):
        l,r=map(int,input().split())
        queries.append([l,r])
    SquareRootDecomposition(n,arr,q,queries)


main()


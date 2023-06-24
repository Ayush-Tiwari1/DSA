#Square Root Decomposition Point Updates in sum

import math

'''
16
2 3 -1 9 6 -2 10 4 12 -1 5 7 16 -4 8 3
3
f 6 13
u 8 -3
f 6 13

Output:

Query 1:	f (6,13)	Sum: 49
Query 2:	u (8,-3)	Update Successfully
Query 3:	f (6,13)	Sum: 46

'''

def SquareRootDecomposition(n,arr,q,queries):
    len=math.ceil(n**0.5)
    sqrt=[0 for i in range(len)]
    for i in range(n):
        sqrtindx=i//len
        sqrt[sqrtindx]+=arr[i]
    
    for i in range(q):
        query,l,r=queries[i]
        print('Query',' ',i+1,':',sep='',end="\t")
        print(query,' ','(',l,',',r,')',sep='',end="\t")
        if query=='u':
            sqrtindx=l//len
            sqrt[sqrtindx]+=r
            arr[l]+=r
            print('Update Successfully')
            
        elif query=='f':
            sum=0
            while l<=r:
                if l%len==0 and (l+len-1)<=r:
                    sum+=sqrt[l//len]
                    l+=len
                else:
                    sum+=arr[l]
                    l+=1
            print('Sum:',sum)

def main():
    n=int(input())
    arr=list(map(int,input().split()))
    q=int(input())
    queries=[]
    for i in range(q):
        inputs=input().split()
        query=inputs[0]
        l=int(inputs[1])
        r=int(inputs[2])
        queries.append([query,l,r])
    
    SquareRootDecomposition(n,arr,q,queries)


main()

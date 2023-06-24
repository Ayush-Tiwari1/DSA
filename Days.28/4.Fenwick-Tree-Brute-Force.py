#Fenwick Tree 
#Brute Force: 
# Preprocessing O(nlogn) ----> n Elements update ( O(logn))
# Update  :   O(logn)
# Sum     :   O(logn)

'''
16 ---> n elements
3
1 
5
-2
-1
4
6
-5
3
8
-6
-7
2
9
6
-4
3---> q queries
s 3 12
u 6 -3
s 3 12


Output:

[0, 3, 4, 5, 7, -1, 3, 6, 11, 3, 11, -6, -2, 2, 11, 6, 22]
Query 1 :	3 12	Sum: 5
Query 2 :	6 -3	Update Successfully
Query 3 :	3 12	Sum: 2

'''



def Sum(i,farr,n):
    sum=0
    while i>0:
        sum+=farr[i]
        i=i-( i & -i)
    return sum
    
def Update(i,val,farr,n):
    while i<=n:
        farr[i]+=val
        i= i+ (i & -i)
    

def FenwickTree(n,arr,q,queries):
    farr=[0 for i in range(n)]
    for i in range(1,n):
        Update(i,arr[i],farr,n)
    print(farr)
    for i in range(q):
        query,l,r=queries[i]
        print('Query',i+1,":",end="\t")
        print(l,r,end="\t")
        if query=='u':
            Update(l,r,farr,n)
            print('Update Successfully')
        elif query=='s':
            s1=Sum(r,farr,n)
            s2=Sum(l-1,farr,n)
            print('Sum:',s1-s2)
    

def main():
    n=int(input())
    arr=[None]
    for i in range(n):
        val=int(input())
        arr.append(val)
    q=int(input())
    queries=[]
    for i in range(q):
        inputs=input().split()
        query=inputs[0]
        l=int(inputs[1])
        r=int(inputs[2])
        queries.append([query,l,r])
    FenwickTree(n+1,arr,q,queries)

main()
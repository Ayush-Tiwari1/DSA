# Segment Tree
# Time Complexities:
# Update    :   O(logn)
# Find      :   O(logn)

import sys


def BuildSegmentTree(indx,low,high,arr,segtree):
    if low==high:
        segtree[indx]=arr[low]
        return segtree[indx]
    mid=(low+high)//2
    left=BuildSegmentTree(2*indx+1,low,mid,arr,segtree)
    right=BuildSegmentTree(2*indx+2,mid+1,high,arr,segtree)
    segtree[indx]=min(left,right)
    return segtree[indx]

def Find(indx,l,r,low,high,segtree):
    #No Overlap
    if high<l or low>r:
        return sys.maxsize
    
    #Complete Overlap
    elif low>=l and high<=r:
        return segtree[indx]
    
    #Partial Complete
    else:
        mid=(low+high)//2
        left=Find(2*indx+1,l,r,low,mid,segtree)
        right=Find(2*indx+2,l,r,mid+1,high,segtree)
        return min(left,right)
        

def Update(indx,i,val,low,high,segtree):
    if high<i or low>i:
        return segtree[indx]
    if low==high:
        segtree[indx]=val
        return val
    mid=(low+high)//2
    left=Update(2*indx+1,i,val,low,mid,segtree)
    right=Update(2*indx+2,i,val,mid+1,high,segtree)
    segtree[indx]=min(left,right)
    return segtree[indx]
        
        


def main():
    n=int(input())
    arr=list(map(int,input().split()))
    segtree=[-1 for i in range(4*n)]
    BuildSegmentTree(0,0,n-1,arr,segtree)
    print(segtree)
    q=int(input())
    for i in range(q):
        inputs=input().split()
        query=inputs[0]
        l=int(inputs[1])
        r=int(inputs[2])
        print('Query',i+1,':','Find' if query=='f' else 'Update')
        # 'f' -----> Find Query
        if query=='f':
            if l>=0 and r<n:
                val=Find(0,l,r,0,n-1,segtree)
                print('Min in range: ','(',l,',',r,') is ',val,sep='')
            else:
                print('Range ','(',l,',',r,')', ' is not Appropriate',sep='')
        elif query=='u':
            print('indx= ',l,' val= ',r,sep='',end='\t')
            if l>=0 and l<n:
                Update(0,l,r,0,n-1,segtree)
                
                print('Update Successfully')
            else:
                print('Cannot Update')
        

main()

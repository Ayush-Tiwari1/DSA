#Inversion Count using Merge Sort in O(nlogn)
# Inversion Count ----> i< j but a[i]> a[j] 
# Inversion Count shows how far array is from being sorted.


'''
n=42
arr=[468 335 1 170 225 479 359 463 465 206 146 282 328 462 492 496
     443 328 437 392 105 403 154 293 383 422 217 219 396 448 227 
     272 39 370 413 168 300 36 395 204 312 323]
     
Output: 494
'''

def Merge(start,mid,end,count,a,b):
    i=start
    k=start
    j=mid+1
    while i<=mid and j<=end:
        if a[i]<=a[j]:
            b[k]=a[i]
            i+=1
        else:
            count[0]+=(mid-i+1)
            b[k]=a[j]
            j+=1
        k+=1
    while i<=mid:
        b[k]=a[i]
        i+=1
        k+=1
    while j<=end:
        b[k]=a[j]
        j+=1
        k+=1
    
    for i in range(start,end+1):
        a[i]=b[i]
    

def MergeSort(start,end,count,a,b):
    if start<end:
        mid=(start+end)//2
        MergeSort(start,mid,count,a,b)
        MergeSort(mid+1,end,count,a,b)
        Merge(start,mid,end,count,a,b)


def main():
    n=int(input())
    a=list(map(int,input().split()))
    b=[0 for i in range(n)]
    count=[0]
    MergeSort(0,n-1,count,a,b)
    for i in range(n):
        print(a[i],end=" ")
    print()
    print(count[0])

main()
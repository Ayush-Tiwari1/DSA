#Merge Sort

def Merge(start,mid,end,a,b):
    i=start
    k=start
    j=mid+1
    while i<=mid and j<=end:
        if a[i]<a[j]:
            b[k]=a[i]
            i+=1
        else:
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
    

def MergeSort(start,end,a,b):
    if start<end:
        mid=(start+end)//2
        MergeSort(start,mid,a,b)
        MergeSort(mid+1,end,a,b)
        Merge(start,mid,end,a,b)


def main():
    n=int(input())
    a=list(map(int,input().split()))
    b=[0 for i in range(n)]
    MergeSort(0,n-1,a,b)
    for i in range(n):
        print(a[i],end=" ")


main()
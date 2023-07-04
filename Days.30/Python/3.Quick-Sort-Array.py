# Quick Sort using Haore's Parition
# Time Complexity:
# O(n*n)    ---> Worst Case
# O(nlogn)  ---> Average Case

# Haore's Partition
def Partition(arr,low,high):
    pivot=low
    i=low
    j=low+1
    while j<=high:
        if arr[j]<=arr[pivot]:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
        j+=1
    arr[i],arr[pivot]=arr[pivot],arr[i]
    return i


def QuickSort(arr,low,high):
    if low<high:
        m=Partition(arr,low,high)
        QuickSort(arr,low,m-1)
        QuickSort(arr,m+1,high)


def main():
    n=int(input())
    arr=list(map(int,input().split()))
    QuickSort(arr,0,n-1)
    print(arr)



main()


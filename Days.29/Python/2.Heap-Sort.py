# Heap Sort 
# Time Complexity: O(nlogn)
# Space Complexity: O(1)


def Heapify(i,n,arr):
    smallest=i
    left=2*i+1
    right=2*i+2
    if left<n and arr[left]<arr[smallest]:
        smallest=left
    if right<n and arr[right]<arr[smallest]:
        smallest=right
    if smallest!=i:
        arr[i],arr[smallest]=arr[smallest],arr[i]
        Heapify(smallest,n,arr)
    


def BuildTree(n,arr):
    #BuildTree
    for i in range(n//2-1,-1,-1):
        Heapify(i,n,arr)
    
    
def HeapSort(n,arr):
    #Build Tree
    BuildTree(n,arr)

    #Heap Sort
    for i in range(n):
        arr[0],arr[n-i-1]=arr[n-i-1],arr[0]
        Heapify(0,n-i-1,arr)

def main():
    n=int(input())
    arr=list(map(int,input().split()))
    HeapSort(n,arr)
    print(arr)


main()




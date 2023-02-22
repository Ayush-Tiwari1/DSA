
def PainterPartition(k,n,arr):
    lo=arr[0]
    hi=arr[0]
    for i in range(1,n):
        if lo<arr[i]:
            lo=arr[i]
        hi+=arr[i]
    if k>n:
        return lo
    sum=0
    mid=None
    ans=-1
    painters=None
    while lo<=hi:
        mid=int((lo+hi)/2)
        sum=0
        painters=1
        for i in range(n):
            sum+=arr[i]
            if sum>mid:
                painters+=1
                sum=arr[i]
        if painters>k:
            lo=mid+1
        else:
            hi=mid-1
            ans=mid
    
    return ans

def main():
    T =int(input())
    for _ in range(T):
        k,n=map(int,input().strip().split())
        arr=[int(x) for x in input().strip().split()]
        # print(k,type(k))
        # print(n,type(n))
        # print(arr,type(arr))
        ans=PainterPartition(k,n,arr)
        print(ans)

if __name__=='__main__':
    main()
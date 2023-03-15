

#O(n*n) ---> TC
#O(n)   ---> SC
def LIS(n,arr):
    dp=[0 for i in range(n)]
    dp[0]=1
    maxi=0
    overall_max=1
    for i in range(1,n):
        maxi=0
        for j in range(0,i):
            if arr[j]<arr[i] and dp[j]>maxi:
                maxi=dp[j]
        dp[i]=maxi+1
        if dp[i]>overall_max:
            overall_max=dp[i]
    return overall_max



#O(nlogn) --> TC
#O(n)     --> SC
def LIS2(n,arr):
    def Ceil(val,dp):
            lo=0
            hi=len(dp)-1
            mid=None
            while lo<=hi:
                mid=(lo+hi)//2
                if dp[mid]==val:
                    return mid
                elif dp[mid]<val:
                    lo=mid+1
                else:
                    hi=mid-1
            return hi+1
    dp=[]
    dp.append(arr[0])
    for i in range(1,n):
        if arr[i]>dp[len(dp)-1]:
            dp.append(arr[i])
        else:
            indx=Ceil(arr[i],dp)
            dp[indx]=arr[i]
    return len(dp)
    
    
def main():
    T=int(input())
    for _ in range(T):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        # print(n,type(n))
        # print(arr,type(arr))
        ans=LIS2(n,arr)
        print(ans)

if __name__=='__main__':
    main()
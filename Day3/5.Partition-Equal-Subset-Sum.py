
def PartitionEqualSubsetSum(n,arr):
    def TargetSumSubset(n,arr,sum):
        dp=[[False]*(sum+1) for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(0,sum+1):
                if j==0:
                    dp[i][j]=True
                elif j<arr[i-1]:
                    dp[i][j]=dp[i-1][j]
                else:
                    if dp[i-1][j]==True or dp[i-1][j-arr[i-1]]==True:
                        dp[i][j]=True
                    else:
                        dp[i][j]=False
        return dp[n][sum]
    
    sum=0
    for i in range(n):
        sum+=arr[i]
    if sum%2 !=0:
        return False
    return TargetSumSubset(n,arr,sum//2)

def main():
    T=int(input())
    for _ in range(T):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ans=PartitionEqualSubsetSum(n,arr)
        if ans == True:
            print('YES')
        else:
            print('NO')

if __name__=='__main__':
    main()
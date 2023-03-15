

def main():
    def CountSumSubset(n,sum,arr):
        dp=[[0]*(sum+1) for i in range(n+1)]
        dp[0][0]=1
        mod=10**9+7
        for i in range(1,n+1):
            for j in range(0,sum+1):
                if j<arr[i-1]:
                    dp[i][j]=dp[i-1][j]%mod
                else:
                    dp[i][j]=(dp[i-1][j]+dp[i-1][j-arr[i-1]])%mod
        # print(dp)
        return dp[n][sum]%mod
    n,sum=map(int,input().split())
    arr=list(map(int,input().strip().split()))
    ans=CountSumSubset(n,sum,arr)
    print(ans)

if __name__=='__main__':
    main()
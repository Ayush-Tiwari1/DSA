
def main():
    def DistinctBinary(n):
        dp=[[0]*n for i in range(2)]
        #Comment
        # dp=[]
        # for i in range(2):
        #     dp.append([int(x) for x in range(n)])
        dp[0][0]=1
        dp[1][0]=1
        mod=10**9+7
        for i in range(1,n):
            dp[0][i]=(dp[0][i-1]+dp[1][i-1])%mod
            dp[1][i]=dp[0][i-1]%mod
        print(dp)
        return (dp[0][n-1]+dp[1][n-1])%mod

    n=int(input())
    ans=DistinctBinary(n)
    print(ans)

if __name__=='__main__':
    main()
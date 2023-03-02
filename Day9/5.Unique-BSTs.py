

def main():
    def UniqueBSTs(n):
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        mod=10**9+7
        for i in range(2,n+1):
            for j in range(0,i):
                dp[i]=(dp[i]+dp[j]*dp[i-j-1])%mod
        return dp[n]%mod
                
    n=int(input())
    ans=UniqueBSTs(n)
    print(ans)

if __name__=='__main__':
    main()
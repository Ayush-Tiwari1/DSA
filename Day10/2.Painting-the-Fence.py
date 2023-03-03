

def main():
    def PaintingFence(n,k):
        if n==1:
            return k
        mod=10**9+7
        dp=[]
        for i in range(n+1):
            dp.append([0,0])
        dp[2][0]=k
        dp[2][1]=k*(k-1)
        for i in range(3,n+1):
            dp[i][0]=dp[i-1][1]%mod
            dp[i][1]=((dp[i-1][0]+dp[i-1][1])*(k-1))%mod
        return (dp[n][0]+dp[n][1])%mod
    n,k=map(int,input().split())
    ans=PaintingFence(n,k)
    print(ans)

if __name__=='__main__':
    main()
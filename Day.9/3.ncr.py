

def main():
    #O(n*r)--->TC
    #O(r)-->SC
    def BinomialCoefficient1(n,r):
        #Using Pascal's Triangle
        if r>n:
            return 0
        dp=[[1]*(r+1) for i in range(n+1)]
        mod=10**9+7
        for i in range(1,n+1):
            for j in range(1,min(i,r+1)):
                dp[i][j]=(dp[i-1][j]+dp[i-1][j-1])%mod
        print(dp)
        return dp[n][r]%mod
    #O(n)-->TC
    #O(1)-->SC
    def BinomialCoefficient2(n,r):
        if r>n:
            return 0
        mod=10**9+7
        r=min(r,n-r)
        #ncr=n!/(n-r)!*r!
        #n * n-1 * n-2 * .... * n-r+1/ 1*2*3 *..*r
        ans=1
        for i in range(r):
            ans=ans*(n-i)
            ans=ans//(i+1)
            ans=ans
        return ans%mod
        
    n,r=map(int,input().split())
    ans=BinomialCoefficient2(n,r)
    print(ans)

if __name__=='__main__':
    main()
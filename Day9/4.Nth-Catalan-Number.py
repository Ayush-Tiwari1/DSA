

def main():
    #O(n)--->TC
    #O(n)--->SC
    def NthCatalanNumber1(n):
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            for j in range(0,i):
                dp[i]+=dp[j]*dp[i-j-1]
        print(dp)
        return dp[n]
    def ncr(n,r):
        ans=1
        r=min(r,n-r)
        for i in range(0,r):
            ans=ans*(n-i)
            ans=ans//(i+1)
        return ans
    #O(n)--->TC
    #O(1)--->SC
    def NthCatalanNumber2(n):
        ans=ncr(2*n,n)
        ans=ans//(n+1)
        return ans
        
    n=int(input())
    ans=NthCatalanNumber2(n)
    print(ans)
    


if __name__=='__main__':
    main()
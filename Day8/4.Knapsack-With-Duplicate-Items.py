

def main():
    def KnapsackWithDuplicateItems(n,w,val,wt):
        dp=[0]*(w+1)
        for i in range(1,w+1):
            dp[i]=0
            for j in range(n):
                if wt[j]<=i:
                    dp[i]=max(dp[i],val[j]+dp[i-wt[j]])
        print(dp)
        return dp[w]
    n,w=map(int,input().split())
    val=[int(x) for x in input().split()]
    wt=list(map(int,input().split()))
    ans=KnapsackWithDuplicateItems(n,w,val,wt)
    print(ans)

if __name__=='__main__':
    main()
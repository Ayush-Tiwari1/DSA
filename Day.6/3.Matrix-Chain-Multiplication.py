


def main():
    def MatrixChainMultiplication(n,arr):
        dp=[[0]*(n-1) for i in range(n-1)]
        for g in range(1,n-1):
            for i,j in zip(range(0,n),range(g,n-1)):
                if g==1:
                    dp[i][j]=arr[i]*arr[j]*arr[j+1]
                else:
                    dp[i][j]=2**63
                    for k in range(i,j):
                        dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+arr[i]*arr[k+1]*arr[j+1])
        return dp[0][n-2]
        
    n=int(input())
    arr=list(map(int,input().strip().split()))
    ans=MatrixChainMultiplication(n,arr)
    print(ans)

if __name__=='__main__':
    main()


def main():
    def CountPalindromicSubsequence(str):
        n=len(str)
        mod=10**9+7
        dp=[[0]*n for i in range(n)]
        for g in range(0,n):
            for i,j in zip(range(0,n),range(g,n)):
                if g==0:
                    dp[i][j]=1
                elif g==1:
                    if str[i]==str[j]:
                        dp[i][j]=3
                    else:
                        dp[i][j]=2
                else:
                    if str[i]==str[j]:
                        dp[i][j]=(dp[i][j-1]+dp[i+1][j]+1)%mod
                    else:
                        dp[i][j]=(dp[i][j-1]+dp[i+1][j]-dp[i+1][j-1])%mod
        # print(dp)
        return dp[0][n-1]%mod
    str=input()
    ans=CountPalindromicSubsequence(str)
    print(ans)

if __name__ =='__main__':
    main()



def main():
    def LongestRepeatingSubsequence(str):
        n=len(str)+1
        dp=[[0]*n for i in range(n)]
        for i in range(1,n):
            for j in range(1,n):
                if i!=j and str[i-1]==str[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        return dp[n-1][n-1]
    str=input()
    ans=LongestRepeatingSubsequence(str)
    print(ans)

if __name__=='__main__':
    main()
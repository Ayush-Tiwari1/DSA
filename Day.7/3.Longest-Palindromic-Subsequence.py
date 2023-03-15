

def main():
    def LongestPalindromicSubsequence(str):
        n=len(str)
        dp=[]
        for i in range(n):
            list=[]
            for j in range(n):
                list.append(0)
            dp.append(list)
        for g in range(n):
            for i,j in zip(range(0,n),range(g,n)):
                if g==0:
                    dp[i][j]=1
                elif g==1:
                    if str[i]==str[j]:
                        dp[i][j]=2
                    else:
                        dp[i][j]=1
                else:
                    if str[i]==str[j]:
                        dp[i][j]=dp[i+1][j-1]+2
                    else:
                        dp[i][j]=max(dp[i][j-1],dp[i+1][j])
        return dp[0][n-1]
    str=input()
    ans=LongestPalindromicSubsequence(str)
    print(ans)

if __name__=='__main__':
    main()
#Minimum Number of character needed to form a Palindrome


def main():
    def FormPalindrome(str):
        n=len(str)
        dp=[[0]*n for i in range(n)]
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
                        dp[i][j]=max(dp[i+1][j],dp[i][j-1])
        return n-dp[0][n-1]
    str=input()
    ans=FormPalindrome(str)
    print(ans)

if __name__=='__main__':
    main()
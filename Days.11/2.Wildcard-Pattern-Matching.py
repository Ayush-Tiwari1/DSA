
class Solution:
    def wildCard(self,pattern, string):
        n=len(pattern)
        m=len(string)
        dp=[[False]*(m+1) for i in range(n+1)]
        dp[0][0]=True
        for i in range(1,n+1):
            for j in range(m+1):
                if j==0:
                    if pattern[i-1]=='*':
                        dp[i][j]=dp[i-1][j]
                    else:
                        dp[i][j]=False
                else:
                    if pattern[i-1]=='*':
                        dp[i][j]=dp[i-1][j] or dp[i][j-1]
                    elif pattern[i-1]=='?':
                        dp[i][j]=dp[i-1][j-1]
                    elif pattern[i-1] == string[j-1]:
                        dp[i][j]=dp[i-1][j-1]
                    else:
                        dp[i][j]=False
        return dp[n][m]



if __name__=='__main__':
    t = int(input())
    for i in range(t):
        pattern = input().strip()
        string = input().strip()
        if Solution().wildCard(pattern, string):
            print(1)
        else:
            print(0)
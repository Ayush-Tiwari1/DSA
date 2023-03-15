
def EditDistance(s,t):
    n1=len(s)+1
    n2=len(t)+1
    dp=[[0]*n2 for i in range(n1)]
    for i in range(n1):
        for j in range(n2):
            if i==0:
                dp[i][j]=j
            elif j==0:
                dp[i][j]=i
            elif s[i-1]==t[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=min(dp[i-1][j-1],min(dp[i-1][j],dp[i][j-1]))+1
    return dp[n1-1][n2-1]

def main():
    T=int(input())
    for _ in range(T):
        s,t=input().split()
        ans=EditDistance(s,t)
        print(ans)

if __name__=='__main__':
    main()
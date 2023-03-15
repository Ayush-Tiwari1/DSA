

def LongestCommonSubstring(n,m,s1,s2):
    dp=[[0]*(m+1) for i in range(n+1)]
    overall_max=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            overall_max=max(overall_max,dp[i][j])
    return overall_max

def main():
    n,m =map(int,input().split())
    s1=input()
    s2=input()
    ans=LongestCommonSubstring(n,m,s1,s2)
    print(ans)

if __name__=='__main__':
    main()
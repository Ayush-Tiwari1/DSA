
def LCS(n1,n2,s1,s2):
    dp=[[0]*(n2+1) for i in range(n1+1)]
    # print(dp)
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[n1][n2]
def main():
    T=int(input())
    for _ in range(T):
        n1,n2=map(int,input().split())
        s1=input()
        s2=input()
        ans=LCS(n1,n2,s1,s2)
        print(ans)

if __name__=='__main__':
    main()
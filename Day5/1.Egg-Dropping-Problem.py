

def main():
    def EggDropping(e, f):
        dp=[[0]*(f+1) for i in range(e+1)]
        for i in range(1,f+1):
            dp[1][i]=i
        for i in range(1,e+1):
            dp[i][1]=1
        INT_MAX=32767
        for i in range(2,e+1):
            for j in range(2,f+1):
                dp[i][j]=INT_MAX
                for k in range(1,j+1):
                    res=max(dp[i-1][k-1],dp[i][j-k])
                    if res<dp[i][j]:
                        dp[i][j]=res+1
        return dp[e][f]
    e,f=map(int,input().split())
    ans=EggDropping(e,f)
    print(ans)

if __name__=='__main__':
    main()
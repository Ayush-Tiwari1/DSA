
def main():
    def LargestSquare(mat,n,m):
        largest=0
        dp=[[0]*m for i in range(n)]
        # print(mat)
        for i in range(n):
            dp[i][m-1]=mat[i][m-1]
        for j in range(m):
            dp[n-1][j]=mat[n-1][j]
        # print(dp)
        for i in range(n-2,-1,-1):
            for j in range(m-2,-1,-1):
                if mat[i][j]==0:
                    dp[i][j]=0
                else:
                    dp[i][j]=min(dp[i+1][j+1],min(dp[i+1][j],dp[i][j+1]))+1
                    largest=max(largest,dp[i][j])
        # print(dp)
        return largest
    n,m=map(int,input().split())
    arr=list(map(int,input().strip().split()))
    mat=[[0]*m for i in range(n)]
    count=0
    for i in range(n):
        for j in range(m):
            mat[i][j]=arr[count]
            count+=1
    ans=LargestSquare(mat,n,m)
    print(ans)


if __name__=='__main__':
    main()
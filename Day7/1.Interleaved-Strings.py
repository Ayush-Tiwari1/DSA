

def main():
    def InterleavedStrings(A,B,C):
        n1=len(A)
        n2=len(B)
        n3=len(C)
        if n1+n2 != n3:
            return -1
        dp=[[False]*(n2+1) for i in range(n1+1)]
        for i in range(n1+1):
            for j in range(n2+1):
                if i==0 and j==0:
                    dp[i][j]=True
                elif i==0:
                    if B[j-1]==C[j-1]:
                        dp[i][j]=True
                    else:
                        dp[i][j]=False
                elif j==0:
                    if A[i-1] == C[i-1]:
                        dp[i][j]=True
                    else:
                        dp[i][j]=False
                elif A[i-1]==C[i+j-1] and B[j-1]==C[i+j-1]:
                    dp[i][j]=dp[i-1][j] or dp[i][j-1]
                elif A[i-1]==C[i+j-1]:
                    dp[i][j]=dp[i-1][j]
                elif B[j-1]==C[i+j-1]:
                    dp[i][j]=dp[i][j-1]
                else:
                    dp[i][j]=False
        # print(dp)
        return dp[n1][n2]  

    A,B,C= input().split()
    ans=InterleavedStrings(A,B,C)
    print(ans)

if __name__=='__main__':
    main()

class Solution:
    def sequenceCount(self,arr1, arr2):
        S=arr1
        T=arr2
        n=len(arr1)
        m=len(arr2)
        dp=[[0 for i in range(n+1)] for j in range(m+1)]
        # print(dp)
        mod=10**9+7
        for i in range(m+1):
            dp[i][0]=0
        for j in range(n+1):
            dp[0][j]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if T[i-1]!=S[j-1]:
                    dp[i][j]=dp[i][j-1]%mod
                else:
                    dp[i][j]=(dp[i][j-1]+dp[i-1][j-1])%mod
        return dp[m][n]%mod
                

import sys
sys.setrecursionlimit(10**6)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr = input().strip().split()
        print(Solution().sequenceCount(str(arr[0]), str(arr[1])))

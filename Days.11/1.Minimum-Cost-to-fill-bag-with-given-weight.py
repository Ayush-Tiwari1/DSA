
class Solution:
    def minimumCost(self, cost, n, W):
        INT_MAX=2**63
        dp=[[INT_MAX]*(W+1) for i in range(n+1)]
        dp[0][0]=0
        for i in range(1,n+1):
            for j in range(0,W+1):
                if j==0:
                    dp[i][j]=0
                else:
                    if j<i or cost[i-1] == -1:
                        dp[i][j]=dp[i-1][j]
                    else:
                        dp[i][j]=dp[i-1][j]
                        if dp[i-1][j-i]!=INT_MAX:
                            dp[i][j]=min(dp[i][j],cost[i-1]+dp[i-1][j-i])
        # print(dp)
        if dp[n][W]==INT_MAX:
            return -1
        return dp[n][W]

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,w = input().split()
		n,w = int(n),int(w)
		a = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minimumCost(a,n,w)
		print(ans)
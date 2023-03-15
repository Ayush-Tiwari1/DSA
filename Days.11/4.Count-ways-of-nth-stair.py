

class Solution:
      def nthStair(self,n):
        dp=[1]*(n+1)
        for i in range(2,n+1):
            dp[i]+=dp[i-2]
        return dp[n]




import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.nthStair(n)
		print(ans)

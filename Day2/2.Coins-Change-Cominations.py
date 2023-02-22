
class Solution:
    def count(self, coins, N, Sum):
        #One way to create array with 0 value
        dp=[0]*(Sum+1)
        # print(sum1)
        #Second way to create array with 0 value
        # sum2=[0 for x in range(Sum+1)]
        # print(sum2)
        dp[0]=1
        for i in range(N):
            for j in range(coins[i],Sum+1):
                dp[j]+=dp[j-coins[i]]
        return dp[Sum]



import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

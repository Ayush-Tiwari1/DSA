# Buy and Sell a Share at most K Transactions Allowed
'''
n=6
prices=[10 22 5 75 65 80]
k=2

Output: 87 
        [Buy  Sell]
        [10     22] ---> 12
        [5      80] ---> 75
        ---------------------
            Total   ---> 87
        ---------------------
'''

def KTransactions(n,k,prices):
    dp=[[0 for j in range(n)] for i in range(k+1)]
    
    for i in range(1,k+1):
        maxi=-2**63
        for j in range(1,n):
            maxi=max(maxi,dp[i-1][j-1]-prices[j-1])
            dp[i][j]=max(dp[i][j-1],maxi+prices[j])
    
    for i in range(k+1):
        for j in range(n):
            print(dp[i][j],end="\t")
        print()
    return dp[k][n-1]
    
def main():
    n=int(input())
    prices=list(map(int,input().split()))
    k=int(input())
    ans=KTransactions(n,k,prices)
    print(ans)
    


main()
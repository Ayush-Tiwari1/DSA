

def main():
    def TargetSumSubset(n,arr,sum):
            dp=[[False]*(sum+1) for i in range(n+1)]
            dp[0][0]=True
            for i in range(1,n+1):
                for j in range(0,sum+1):
                    if j==0:
                        dp[i][j]=True
                    elif j<arr[i-1]:
                        dp[i][j]=dp[i-1][j]
                    else:
                        dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
            
            return dp
    n=int(input())
    arr=[int(x) for x in input().strip().split()]
    sum=0
    for i in range(n):
        sum+=arr[i]
    dp=TargetSumSubset(n,arr,sum)
    max_indx=0
    for i in range(0,sum//2+1):
        if dp[n][i]==True:
            max_indx=i
    print(sum-2*max_indx)

if __name__=='__main__':
    main()
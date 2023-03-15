#Rod Cutting
def RodCutting(n,price):
    dp=[0 for i in range(n)]
    dp[0]=price[0]
    end=max=None
    overallmax=price[0]
    for i in range(1,n):
        max=price[i]
        end=i-1
        for start in range(int(i/2)+1):
            if dp[start]+dp[end-start]>max:
                max=dp[start]+dp[end-start]
        dp[i]=max
        if max>overallmax:
            overallmax=max
    # print(dp)
    return overallmax

def main():
    T=int(input())
    for _ in range(T):
        n=int(input())
        price=[int(x) for x in input().strip().split()]
        ans=RodCutting(n,price)
        print(ans)
if __name__ == '__main__':
    main()
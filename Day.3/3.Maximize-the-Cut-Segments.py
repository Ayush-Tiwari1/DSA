
def MaximizeCutSegments(n,x,y,z):
    dp=[-1]*(n+1)
    dp[0]=0
    dp[n]=0
    arr=[]
    arr.append(x)
    arr.append(y)
    arr.append(z)
    for i in range(3):
        for j in range(arr[i],n+1):
            if dp[j-arr[i]] !=-1 and dp[j]<=dp[j-arr[i]]:
                dp[j]=dp[j-arr[i]]+1
    return dp[n]


def main():
    T=int(input())
    for _ in range(T):
        n=int(input())
        x,y,z= map(int,input().split())
        ans=MaximizeCutSegments(n,x,y,z)
        print(ans)

if __name__=='__main__':
    main()
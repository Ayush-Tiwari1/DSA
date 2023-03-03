

def main():
    def LongestBitonicSubsequence(n,arr):
        #Longest Increasing Subsequence
        lis=[0]*n
        lis[0]=1
        for i in range(1,n):
            maxi=0
            for j in range(0,i):
                if arr[j]<arr[i]:
                    maxi=max(maxi,lis[j])
            lis[i]=maxi+1
        # print(lis)
        #Longest Decreasing Subsequence
        lds=[0]*n
        lds[n-1]=1
        for i in range(n-2,-1,-1):
            maxi=0
            for j in range(i+1,n):
                if arr[j]<arr[i]:
                    maxi=max(maxi,lds[j])
            lds[i]=maxi+1
        # print(lds)
        ans=0
        for i in range(n):
            ans=max(ans,(lis[i]+lds[i])-1)
        return ans
    n=int(input())
    arr=list(map(int,input().split()))
    ans=LongestBitonicSubsequence(n,arr)
    print(ans)


if __name__=='__main__':
    main()
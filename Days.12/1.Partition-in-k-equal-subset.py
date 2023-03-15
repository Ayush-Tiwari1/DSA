

class Solution:
    def __init__(self):
        self.flag=False
    def KPartition(self,indx,n,a,k,subsetsum,dp,nos):
        if indx==n:
            if nos==k:
                for i in range(k-1):
                    if subsetsum[i]!=subsetsum[i+1]:
                        return
                self.flag=True
            return
        
        for i in range(k):
            if len(dp[i])==0:
                subsetsum[i]+=a[indx]
                dp[i].append(a[indx])
                self.KPartition(indx+1,n,a,k,subsetsum,dp,nos+1)
                subsetsum[i]-=a[indx]
                dp[i].pop()
                break
            else:
                subsetsum[i]+=a[indx]
                dp[i].append(a[indx])
                self.KPartition(indx+1,n,a,k,subsetsum,dp,nos)
                subsetsum[i]-=a[indx]
                dp[i].pop()
    def isKPartitionPossible(self, a, k):
        subsetsum=[0]*k
        dp=[[] for i in range(k)]
        self.KPartition(0,len(a),a,k,subsetsum,dp,0)
        return self.flag



if __name__ == '__main__':
    tcs = int(input())
    for _ in range(tcs):
        N=int(input())
        arr=[int(x) for x in input().split()]
        k=int(input())
        if Solution().isKPartitionPossible(arr, k):
            print(1)
        else:
            print(0)

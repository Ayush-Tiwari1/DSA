
class Solution:
    def longestSubsequence(self, N, A):
        dict={}
        
        ans=1
        for i in range(N):
            len=1
            if A[i]-1 in dict:
                len=max(len,dict[A[i]-1]+1)
            if A[i]+1 in dict:
                len=max(len,dict[A[i]+1]+1)
            dict[A[i]]=len
            ans=max(ans,len)
        return ans
            


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = input().split()
        for itr in range(N):
            A[itr] = int(A[itr])
        
        ob = Solution()
        print(ob.longestSubsequence(N, A))

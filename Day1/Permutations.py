
class Solution:
    def find_permutation(self, S):
        hmap={}
        ans=[]
        temp=""
        def permutations(S,temp):
            if S == '':
                if temp not in hmap:
                    ans.append(temp)
                    hmap[temp]=1
                return
            for i in range(len(S)):
                left=S[:i]
                right=S[i+1:]
                permutations(left+right,temp+S[i])
        permutations(S,temp)
        ans.sort()
        return ans
        



if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		for i in ans:
			print(i,end=" ")
		print()
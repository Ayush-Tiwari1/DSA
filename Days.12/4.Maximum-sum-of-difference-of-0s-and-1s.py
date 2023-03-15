class Solution:
    def maxSubstring(self, S):
        max_sum = -1
        curr_sum = 0
        for i in range(len(S)):
            if S[i] == '0':
                curr_sum += 1
            else:
                curr_sum -= 1
            max_sum = max(max_sum, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return max_sum


if __name__ == '__main__':
	T = int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.maxSubstring(s)
		print(answer)

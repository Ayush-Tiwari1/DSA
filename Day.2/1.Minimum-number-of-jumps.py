
class Solution:
    def minJumps(self, arr, n):
        if arr[0] == 0:
            return -1
        jumps = 0
        steps = 0
        minreach = 0
        for i in range(n-1):
            if i+arr[i] > minreach:
                minreach = i+arr[i]
            if steps == 0:
                jumps += 1
                if minreach-i == steps:
                    return -1
                steps = minreach-i
            steps -= 1
        return jumps


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr, n)
        print(ans)


class Solution:
    def solve(self, arr, n):
        arr.sort()
        first=0
        second=0
        for i in range(n):
            if i%2==0:
                first=first*10+arr[i]
            else:
                second=second*10+arr[i]
        return first+second


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.solve(arr, n)
        print(ans)
        tc -= 1

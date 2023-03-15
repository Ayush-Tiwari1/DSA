
class Solution:
    def fun(self,s):
        a=0
        ab=0
        abc=0
        mod=10**9+7
        tempa=tempab=tempabc=0
        for i in range(len(s)):
            if s[i]=='a':
                tempa=2*a+1
                a=tempa%mod
            elif s[i]=='b':
                tempab=2*ab+a
                ab=tempab%mod
            else:
                tempabc=2*abc+ab
                abc=tempabc%mod
        return abc%mod



t=int(input())
for _ in range(t):
    s=input()
    print(Solution().fun(s))

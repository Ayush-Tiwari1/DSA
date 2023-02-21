
class Solution:
    def isAnagram(self,a,b):
        hmap={}
        for i in range(len(a)):
            if hmap.get(a[i],0) == 0:
                hmap[a[i]]=1
            else:
                hmap[a[i]]=hmap[a[i]]+1
        for i in range(len(b)):
            if hmap.get(b[i],0) == 0:
                return False
            hmap[b[i]]= hmap[b[i]]-1
        return True
        

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
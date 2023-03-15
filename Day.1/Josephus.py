
import math

class Solution:
    def josephus(self,n,k):
        
        def Josephus(n,k):
            if n==0:
                return 0
            x=Josephus(n-1,k)
            y=(x+k)%n
            return y
        return Josephus(n,k)+1

   
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        nk=[int(x) for x in input().strip().split()]
        n=nk[0]
        k=nk[1]
        
        print(Solution().josephus(n,k))
        
        T-=1

if __name__=="__main__":
    main()
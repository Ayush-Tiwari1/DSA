# Median in a Running Stream

import math, heapq

class Solution:
    def __init__(self):
        self.maxheap=[]
        self.minheap=[]
    
    def BalanceHeaps(self):
        if len(self.minheap)>len(self.maxheap):
            heapq.heappush(self.maxheap,-heapq.heappop(self.minheap))
        elif len(self.maxheap)>len(self.minheap)+1:
            heapq.heappush(self.minheap,-heapq.heappop(self.maxheap))
    def insertHeaps(self,x):
        if len(self.maxheap)==0 or x<-self.maxheap[0]:
            heapq.heappush(self.maxheap,-x)
        else:
            heapq.heappush(self.minheap,x)
        self.BalanceHeaps()

    def getMedian(self):
        if len(self.maxheap)>len(self.minheap):
            return -self.maxheap[0]
        else:
            return (-self.maxheap[0]+self.minheap[0])/2
        
def main():
    n=int(input())
    solution=Solution()
    for i in range(n):
        x=int(input())
        solution.insertHeaps(x)
        print(math.floor(solution.getMedian()))



main()
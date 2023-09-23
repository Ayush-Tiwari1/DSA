# Swim in Rising Water

'''
Input:
5
0   1   2   3   4
24  23  22  21  5
12  13  14  15  16
11  17  18  19  20
10  9   8   7   6

Output:
16
'''



import heapq

class Heap:
    def __init__(self):
        self.heap=[]
    
    def size(self):
        return len(self.heap)
        
    def heappush(self,new_list):
        heapq.heappush(self.heap,(new_list[2],new_list))
    
    def heappop(self):
        return heapq.heappop(self.heap)[1]


def SwimInRisingWater(n,grid):
    visited=[[False for j in range(n)] for i in range(n)]
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    heap=Heap()
    heap.heappush([0,0,grid[0][0]])
    visited[0][0]=True
    while heap.size()>0:
        i,j,maxi=heap.heappop()
        if i==n-1 and j==n-1:
            return maxi
        for k in range(4):
            row=dx[k]+i
            col=dy[k]+j
            if row>=0 and col>=0 and row<n and col<n and visited[row][col]==False:
                visited[row][col]=True
                heap.heappush([row,col,max(maxi,grid[row][col])])
            
    return -1


def main():
    n=int(input())
    grid=[]
    for i in range(n):
        grid.append(list(map(int,input().split())))
    ans=SwimInRisingWater(n,grid)
    print(ans)



if __name__=='__main__':
    main()
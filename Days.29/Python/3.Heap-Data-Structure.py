# Heap Implementation

class Heap:
    def __init__(self):
        self.heap=[]
    
    def size(self):
        return len(self.heap)
    
    def _swap(self,i,j):
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]
        
    def _heapifyUp(self,i):
        smallest=i
        left=2*i+1
        right=2*i+2
        n=self.size()
        if left<n and self.heap[left]<self.heap[smallest]:
            smallest=left
        if right<n and self.heap[right]<self.heap[smallest]:
            smallest=right
        if smallest!=i:
            self._swap(smallest,i)
            self._heapifyUp(smallest)
    
    def _heapifyDown(self,i):
        par=(i-1)//2
        while par>=0 and self.heap[par]>self.heap[i]:
            self._swap(par,i)
            i=par
            par=(i-1)//2
    
    def put(self,val):
        self.heap.append(val)
        self._heapifyDown(self.size()-1)
        
    def get(self):
        n=self.size()
        if n==0:
            print('Heap is Empty')
            return -1
        self._swap(0,n-1)
        val=self.heap.pop()
        self._heapifyUp(0)
        return val
    
    def isempty(self):
        size=self.size()
        if size==0:
            return True
        return False
    
    def peek(self):
        if self.size()==0:
            print('Heap is Empty')
            return -1
        return self.heap[0]
    
    def printHeap(self):
        print(self.heap)


def main():
    print('Min-Heap Data Structure')
    heap=Heap()
    while True:
        print('1.Insert')
        print('2.Delete')
        print('3.Min')
        print('4.isEmpty')
        print('5.size')
        print('6.Print Heap')
        print('7.Exit')
        choice=int(input('Enter Your Choice: '))
        if choice==1:
            val=int(input('Enter a Value: '))
            heap.put(val)
        elif choice==2:
            val=heap.get()
            if val!=-1:
                print('Pop Value is:',val)
        elif choice==3:
            val=heap.peek()
            if val!=-1:
                print('Min Value is:',val)
        elif choice==4:
            if heap.isempty()==True:
                print('Heap is Empty')
            else:
                print('Heap is Not Empty')
        elif choice==5:
            print('Heap Size:',heap.size())
        elif choice==6:
            heap.printHeap()
        elif choice==7:
            break
        else:
            print('Invalid Choice')

main()





class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

    def push(self,x):
        if len(self.s) == 0:
            self.minEle=x
            self.s.append(x)
        else:
            if x>=self.minEle:
                self.s.append(x)
            else:
                self.s.append(2*x-self.minEle)
                self.minEle=x

    def pop(self):
        if len(self.s)==0:
            return -1
        val=0
        if self.s[-1]>=self.minEle:
            val=self.s[-1]
            self.s.pop()
        else:
            val=self.minEle
            self.minEle=2*self.minEle-self.s[-1]
            self.s.pop()
        return val
        

    def getMin(self):
        if len(self.s)==0:
            return -1
        return self.minEle

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        q = int(input())

        arr = [int(x) for x in input().split()]

        stk=stack()  

        qi = 0
        qn=1
        while qn <= q:
            qt = arr[qi]

            if qt == 1:
                stk.push(arr[qi+1])
                qi+=2
            elif qt==2:
                print(stk.pop(),end=' ')
                qi+=1
            else:
                print(stk.getMin(),end=' ')
                qi+=1
            qn+=1
        print()

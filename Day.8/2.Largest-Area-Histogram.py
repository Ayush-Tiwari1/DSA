

def main():
    def LargestAreaHistogram(n,arr):
        nsl=[-1]*n
        lstack=[]
        for i in range(n):
            while len(lstack)!=0 and arr[lstack[-1]]>=arr[i]:
                lstack.pop()
            if len(lstack)==0:
                nsl[i]=-1
            else:
                nsl[i]=lstack[-1]
            lstack.append(i)
        # print(nsl)
        nsr=[n]*n
        rstack=[]
        for i in range(n-1,-1,-1):
            while len(rstack)!=0 and arr[rstack[-1]]>=arr[i]:
                rstack.pop()
            if len(rstack)==0:
                nsr[i]=n
            else:
                nsr[i]=rstack[-1]
            rstack.append(i)
        # print(nsr)
        area=0
        temparea=0
        for i in range(n):
            temparea=(nsr[i]-nsl[i]-1)*arr[i]
            area=max(area,temparea)
            # print(temparea,end=" ")
        # print()
        return area
                
    n=int(input())
    arr=[int(x) for x in input().strip().split()]
    ans=LargestAreaHistogram(n,arr)
    print(ans)
if __name__=='__main__':
    main()
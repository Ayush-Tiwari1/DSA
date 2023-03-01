
from collections import deque
def main():
    def RectangleArea(mat,n,m):
        def LargestAreaHistogram(arr,n):
                nsl=[-1]*n
                lstack=deque()
                for i in range(n):
                    while lstack and arr[lstack[-1]]>=arr[i]:
                        lstack.pop()
                    if lstack:
                        nsl[i]=lstack[-1]
                    else:
                        nsl[i]=-1
                    lstack.append(i)
                # print(nsl)
                nsr=[n]*n
                rstack=deque()
                for i in range(n-1,-1,-1):
                    while len(rstack)!=0 and arr[rstack[-1]]>=arr[i]:
                        rstack.pop()
                    if rstack:
                        nsr[i]=rstack[-1]
                    else:
                        nsr[i]=n
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
        if n==0 or m==0:
            return 0
        rectangle=mat[0]
        # nsl=deque()
        # nsr=deque()
        rectarea=LargestAreaHistogram(rectangle,m)
        for i in range(1,n):
            for j in range(m):
                if mat[i][j]==0:
                    rectangle[j]=0
                else:
                    rectangle[j]+=mat[i][j]
            currarea=LargestAreaHistogram(rectangle,m)
            if currarea>rectarea:
                rectarea=currarea
        return rectarea
    n,m=map(int,input().split())
    mat=[]
    for i in range(n):
        mat.append(list(map(int,input().split())))
    ans=RectangleArea(mat,n,m)
    print(ans)

if __name__=='__main__':
    main()
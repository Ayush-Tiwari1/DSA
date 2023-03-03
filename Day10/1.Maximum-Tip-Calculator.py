

def main():
    def MaximumTipCalculator(a,b,n,x,y):
        def compare(val):
            return val[0]
        Pair=[]
        for i in range(n):
            Pair.append([abs(a[i]-b[i]),i])
        Pair.sort(key=compare,reverse=True)
        ans=0
        for i in range(n):
            indx=Pair[i][1]
            if a[indx]>b[indx]:
                if x>0:
                    ans+=a[indx]
                    x-=1
                elif y>0:
                    ans+=b[indx]
                    y-=1
            else:
                if y>0:
                    ans+=b[indx]
                    y-=1
                elif x>0:
                    ans+=a[indx]
                    x-=1
        return ans
    n,x,y=map(int,input().split(' '))
    a=list(map(int,input().strip().split()))
    b=[int(x) for x in input().strip().split()]
    # print(n,x,y)
    # print(a)
    # print(b)
    ans=MaximumTipCalculator(a,b,n,x,y)
    print(ans)

if __name__=='__main__':
    main()
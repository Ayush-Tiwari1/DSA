

def main():
    def Compare(val):
        return val[1]
    n=int(input())
    start=list(map(int,input().strip().split()))
    end=[int(x) for x in input().strip().split()]
    Pair=[]
    for i in range(n):
        Pair.append([start[i],end[i]])
    Pair.sort(key=Compare)
    temp=Pair[0]
    curr=None
    count=1
    for i in range(1,n):
        curr=Pair[i]
        if temp[1]<curr[0]:
            count+=1
            temp=curr
    print(count)

if __name__=='__main__':
    main()
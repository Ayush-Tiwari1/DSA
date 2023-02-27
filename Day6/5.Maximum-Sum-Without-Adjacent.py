

def main():
    n=int(input())
    arr=[int(x) for x in input().strip().split()]
    val1=arr[0]
    val2=0
    tempval1=tempval2=None
    for i in range(1,n):
        tempval1=val2+arr[i]
        tempval2=max(val1,val2)
        val1=tempval1
        val2=tempval2
    print(max(val1,val2))

if __name__=='__main__':
    main()
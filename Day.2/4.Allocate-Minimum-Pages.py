
def AllocateMinimumPages(n,A,m):
    if m>n:
        return -1
    ans=-1
    lo=A[0]
    hi=A[0]
    for i in range(1,n):
        if A[i]>lo:
            lo=A[i]
        hi+=A[i]
    mid=None
    sum=0
    student=None
    while lo<=hi:
        mid=int((lo+hi)/2)
        sum=0
        student=1
        for i in range(n):
            sum+=A[i]
            if sum>mid:
                student+=1
                sum=A[i]
        if student>m:
            lo=mid+1
        else:
            hi=mid-1
            ans=mid
    return ans

def main():
    T=int(input())
    for _ in range(T):
        n=int(input())
        A=[int(x) for x in input().strip().split()]
        m=int(input())
        ans=AllocateMinimumPages(n,A,m)
        print(ans)

if __name__ == '__main__':
    main()
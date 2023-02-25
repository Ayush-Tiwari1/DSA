

def main():
    n=int(input())
    if n==1:
        print(1)
        return
    first=1
    second=2
    third=2
    mod=10**9+7
    for i in range(3,n+1):
        third=(second+(i-1)*first)%mod
        first=second%mod
        second=third%mod
    print(second%mod)

if __name__=='__main__':
    main()
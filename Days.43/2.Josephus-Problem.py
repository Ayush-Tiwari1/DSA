# Josephus Problem

def Josephus(n,k):
    if n==1:
        return 0
    ans=Josephus(n-1,k)
    return (ans+k)%n

def main():
    n,k=map(int,input().split())
    # n=7 0 1 2 3 4 5 6 7
    ans=Josephus(n,k)
    print(ans)




if __name__=='__main__':
    main()
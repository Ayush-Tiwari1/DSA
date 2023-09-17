# Minimum Number of Swaps required to sort an Array


def MinimumSwaps(n,arr):
    pairs=[]
    for i in range(n):
        pairs.append([arr[i],i])
    pairs.sort(key=lambda x: x[0])
    count=0
    i=0
    while i<n:
        if pairs[i][1]==i:
            i+=1
        else:
            count+=1
            j=pairs[i][1]
            temp=pairs[i]
            pairs[i]=pairs[j]
            pairs[j]=temp
    return count
        


def main():
    n=int(input())
    arr=list(map(int,input().split()))
    ans=MinimumSwaps(n,arr)
    print(ans)


if __name__=='__main__':
    main()
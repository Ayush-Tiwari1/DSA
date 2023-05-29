#Minimum Swaps to Sort


def main():
    n=int(input())
    arr=list(map(int,input().strip().split()))
    pairs=[]
    for i in range(n):
        pairs.append([arr[i],i])
    pairs.sort()
    count=0
    for i in range(n):
        while pairs[i][1]!=i:
            indx=pairs[i][1]
            pairs[i],pairs[indx]=pairs[indx],pairs[i]
            count+=1
    print(count)



main()
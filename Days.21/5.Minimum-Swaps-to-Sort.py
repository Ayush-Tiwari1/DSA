
def MinSwaps(nums,n):
    pairs=[]
    for i in range(n):
        pairs.append([nums[i],i])
    pairs.sort()
    count=0
    for i in range(n):
        while pairs[i][1]!=i:
            indx=pairs[i][1]
            pairs[i],pairs[indx]=pairs[indx],pairs[i]
            count+=1
    return count

def main():
    n=int(input())
    nums=list(map(int,input().strip().split()))
    ans=MinSwaps(nums,n)
    print(ans)


if __name__=='__main__':
    main()
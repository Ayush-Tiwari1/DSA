# Partition to K Equal Sum Subsets

def Partition(indx,nums,k,pairs,currlist,SubsetSum):
    if indx==len(nums):
        if len(currlist)==k:
            for i in range(0,k-1):
                if SubsetSum[i]!=SubsetSum[i+1]:
                    return
            pairs.append([lst[:] for lst in currlist])
        return
        
    for i in range(len(currlist)):
        currlist[i].append(nums[indx])
        SubsetSum[i]+=nums[indx]
        Partition(indx+1,nums,k,pairs,currlist,SubsetSum)
        currlist[i].pop()
        SubsetSum[i]-=nums[indx]
    
    if len(currlist)<k:
        currlist.append([nums[indx]])
        SubsetSum[len(currlist)-1]+=nums[indx]
        Partition(indx+1,nums,k,pairs,currlist,SubsetSum)
        SubsetSum[len(currlist)-1]-=nums[indx]
        currlist.pop()

def PartitionKEqualSum(nums,k):
    SubsetSum=[0 for i in range(k)]
    pairs=[]
    Partition(0,nums,k,pairs,[],SubsetSum)
    return pairs

def main():
    n=int(input())
    nums=list(map(int,input().split()))
    k=int(input())
    ans=PartitionKEqualSum(nums,k)
    for pair in ans:
        print(pair)



if __name__=='__main__':
    main()
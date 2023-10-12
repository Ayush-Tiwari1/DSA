# Partition into K Subsets

# Algorithm:
# ----> Existing Set Append
# ----> New Set 


def PartitionKSubsets(i,n,k,list):
    if i==n+1:
        if len(list)==k:
            for i in range(k):
                print(list[i],end="")
                if i!=k-1:
                    print(end=" | ")
            print()
        return
    # Existing Set Append
    for j in range(len(list)):
        val=list[j]
        list[j]+=str(i)
        PartitionKSubsets(i+1,n,k,list)
        list[j]=val
    
    # New Set 
    list.append(str(i))
    PartitionKSubsets(i+1,n,k,list)
    list.pop()



def main():
    n,k=map(int,input().split())
    if k>n or n==0 or k==0:
        print(-1)
    PartitionKSubsets(1,n,k,[])




if __name__=='__main__':
    main()
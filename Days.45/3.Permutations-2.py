# Permutations-2
# npr= ncr*(r!)
# Prerequisite: Combinations-1


def Permutations2(indx,count,r,list,visited):
    
    if indx==len(list):
        if count==r:
            ans=''.join(list)
            print(ans)
        return

    # Exclude
    Permutations2(indx+1,count,r,list,visited)

    # Inlclude
    for i in range(r):
        if list[indx]=='-' and visited[i]==False:
            list[indx]=str(i+1)
            visited[i]=True
            Permutations2(indx+1,count+1,r,list,visited)
            visited[i]=False
            list[indx]='-'



def main():
    n=int(input())
    r=int(input())
    list=['-' for i in range(n)]
    visited=[False for i in range(n)]
    Permutations2(0,0,r,list,visited)




if __name__=="__main__":
    main()
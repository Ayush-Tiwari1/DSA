# Print Permutations
#        (n)*(n-1)*(n-2)*.....*(n-r-1)*(n-r)!
# npr=  --------------------------------------
#               (n-r)!
# npr=(n)*(n-1)*(n-2)*....*(n-r-1)!


def PrintPermutations(indx,r,list):
    
    if indx==r:
        ans=''.join(list)
        print(ans)
        return
    
    for i in range(len(list)):
        if list[i]=='-':
            list[i]=str(indx+1)
            PrintPermutations(indx+1,r,list)
            list[i]='-'


def main():
    n=int(input())
    r=int(input())
    list=['-' for i in range(n)]
    PrintPermutations(0,r,list)



if __name__=='__main__':
    main()
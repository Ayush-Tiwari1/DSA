# Combination-1
# ncr ----> n!/((n-r)!*r*)
# r---> identical items
# we doing like permutation but it is combination


def Combinations2(indx,count,r,list):
    
    if count==r:
        ans=''.join(list)
        print(ans)
        return
    
    for i in range(indx,len(list)):
        if list[i]=='-':
            list[i]='i'
            Combinations2(i+1,count+1,r,list)
            list[i]='-'


def main():
    n=int(input())
    r=int(input())
    list=['-' for i in range(n)]
    Combinations2(0,0,r,list)


if __name__=='__main__':
    main()
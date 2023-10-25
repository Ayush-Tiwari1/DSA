# Combinations-1 ------> Include/ Exclude Concept

def Combinations(indx,count,r,list):
    if indx==len(list):
        if count==r:
            ans=''.join(list)
            print(ans)
        return
    #Include 
    list[indx]='i'
    Combinations(indx+1,count+1,r,list)
    list[indx]='-'
    #Exclude
    Combinations(indx+1,count,r,list)

def main():
    n=int(input())
    r=int(input())
    list=['-' for i in range(n)]
    Combinations(0,0,r,list)

if __name__=="__main__":
    main()
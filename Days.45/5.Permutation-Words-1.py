# Permutation-Words-1
# Prerequisite: Permutation-2


def Permutation(indx,n,dict,list,ans):
    
    if indx==n:
        ans=''.join(list)
        print(ans)
        return
    
    
    for key,value in dict.items():
        if value>0:
            list[indx]=key
            dict[key]-=1
            Permutation(indx+1,n,dict,list,ans)
            dict[key]+=1
            list[indx]='-'


def main():
    string=input()
    dict={}
    for char in string:
        if char in dict:
            dict[char]+=1
        else:
            dict[char]=1
    list=['-' for i in range(len(string))]
    ans=[]
    Permutation(0,len(string),dict,list,ans)
    ans.sort()
    for string in ans:
        print(string)



if __name__=='__main__':
    main()
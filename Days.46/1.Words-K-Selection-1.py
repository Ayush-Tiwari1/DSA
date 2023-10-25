# Words K Selection 1


def WordsKSelection(indx,count,k,string,list,ans):
    
    if indx==len(string):
        if count==k:
            ans.append(''.join(list))
        return
    
    # Include
    list[indx]=string[indx]
    WordsKSelection(indx+1,count+1,k,string,list,ans)
    list[indx]=""
    # Exclude
    WordsKSelection(indx+1,count,k,string,list,ans)
    


def main():
    string=input()
    k=int(input())
    distinct=""
    dict={}
    for char in string:
        if char not in dict:
            distinct+=char
        dict[char]=True
    ans=[]
    list=["" for i in range(len(distinct))]
    WordsKSelection(0,0,k,distinct,list,ans)
    for string in ans:
        print(string)


if __name__=='__main__':
    main()
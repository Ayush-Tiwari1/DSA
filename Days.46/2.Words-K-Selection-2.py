# Words-K-Selection-2

def WordsKSelection2(indx,count,k,string,list,visited,ans):
    if indx==len(string):
        if count==k:
            ans.append(''.join(list))
        return
    
    
    for i in range(indx,len(string)):
        if list[indx]=="" and visited[i]==False:
            list[indx]=string[i]
            visited[i]=True
            WordsKSelection2(i+1,count+1,k,string,list,visited,ans)
            visited[i]=False
            list[indx]=""
    WordsKSelection2(i+1,count,k,string,list,visited,ans)
        
    

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
    visited=[False for i in range(len(distinct))]
    WordsKSelection2(0,0,k,distinct,list,visited,ans)
    for string in ans:
        print(string)
    

if __name__=="__main__":
    main()
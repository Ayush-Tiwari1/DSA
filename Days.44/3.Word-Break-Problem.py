# Word Break Problem

def WordBreakHelper(string,temp,dictionary,ans):
    if len(string)==0:
        ans.append(temp)
        return
    s=""
    space=" "
    if len(temp)==0:
        space=""
    for i in range(len(string)):
        s+=string[i]
        if s in dictionary:
            WordBreakHelper(string[i+1:],temp+space+s,dictionary,ans)

def WordBreak(n,dict,string):
    dictionary={}
    for temp in dict:
        dictionary[temp]=True
    ans=[]
    WordBreakHelper(string,"",dictionary,ans)
    return ans


def main():
    n=int(input())
    dict=input().split()
    string=input()
    ans=WordBreak(n,dict,string)
    for pairs in ans:
        print(pairs)



if __name__=='__main__':
    main()
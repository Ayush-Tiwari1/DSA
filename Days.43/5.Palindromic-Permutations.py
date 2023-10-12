# Palindromic Permutations

# All characters must have Even Degree.
# One Odd degree can be possible

def Palindrome(temp,string,ans,set):
    if temp=="":
        if string not in set:
            ans.append(string)
        set.add(string)
        return
    for i in range(len(temp)):
        substr1=temp[0:i]
        substr2=temp[i+1:]
        Palindrome(substr1+substr2,string+temp[i],ans,set)


def PalindromicPermutations(string):
    dict={}
    for char in string:
        if char in dict:
            dict[char]+=1
        else:
            dict[char]=1
    oddcount=0
    oddchar=''
    temp=""
    for key,value in dict.items():
        if value%2!=0:
            oddcount+=1
            oddchar=key
        temp+=((value//2)*key)
    if oddcount>1:
        return []
    st=set()
    ans=[]
    Palindrome(temp,"",ans,st)
    finalans=[]
    for string in ans:
        finalans.append(string+oddchar+string[::-1])
    finalans.sort()
    return finalans


def main():
    string=input()
    ans=PalindromicPermutations(string)
    for string in ans:
        print(string,end=" ")
    print()



if __name__=='__main__':
    main()
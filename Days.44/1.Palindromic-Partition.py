# Palindromic Partitioning of a string

def Palindrome(temp):
    i=0
    j=len(temp)-1
    while i<j:
        if temp[i]!=temp[j]:
            return False
        i+=1
        j-=1
    return True

def PalindromicPartition(string,palin,ans):
    if string=="":
        ans.append(palin)
        return
    temp=""
    for i in range(len(string)):
        temp+=string[i]
        if Palindrome(temp):
            PalindromicPartition(string[i+1:],palin+'('+temp+')',ans)


def main():
    string=input()
    ans=[]
    PalindromicPartition(string,"",ans)
    for palin in ans:
        print(palin)

if __name__=='__main__':
    main()

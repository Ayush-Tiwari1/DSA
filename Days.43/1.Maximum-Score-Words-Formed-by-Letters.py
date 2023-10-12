# Maximum Score Words Formed by Letters


def Subsequence(indx,words,dict,score,curr_score,maxi):
    if indx==len(words):
        maxi[0]=max(maxi[0],curr_score)
        return
    # Include
    flag=True
    scr=0
    includeletters=[]
    for letter in words[indx]:
        if letter in dict and dict[letter]>0:
            dict[letter]-=1
            scr+=score[ord(letter)-ord('a')]
            includeletters.append(letter)
        else:
            flag=False
            break
    if flag:
        Subsequence(indx+1,words,dict,score,curr_score+scr,maxi)
    for letter in includeletters:
        dict[letter]+=1
    
    # Exclude
    Subsequence(indx+1,words,dict,score,curr_score,maxi)




def MaximumScore(words,letters,score):
    maxi=[0]
    dict={}
    for letter in letters:
        if letter in dict:
            dict[letter]+=1
        else:
            dict[letter]=1
    Subsequence(0,words,dict,score,0,maxi)
    return maxi[0]




def main():
    n=int(input())
    words=list(input().split())
    k=int(input())
    letters=list(input().split())
    score=list(map(int,input().split()))
    ans=MaximumScore(words,letters,score)
    print('Maximum Score:',ans)



if __name__=='__main__':
    main()


def main():
    def WordBreak(n,dic,word):
        dictionary={}
        for i in range(n):
            dictionary[dic[i]]=1
        n=len(word)
        dp=[0 for i in range(n+1)]
        dp[0]=1
        for i in range(1,n+1):
            for j in range(i,0,-1):
                if word[j-1:i] in dictionary:
                    dp[i]+=dp[j-1]
        print(dp)
        return dp[n]
    n=int(input())
    dic=list(input().split())
    word=input()
    ans=WordBreak(n,dic,word)
    print(ans)

if __name__=='__main__':
    main()
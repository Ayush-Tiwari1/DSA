

def main():
    def PalindromicPartition(str):
        n=len(str)
        dp=[[False]*n for i in range(n)]
        for g in range(0,n):
            for i,j in zip(range(0,n),range(g,n)):
                if g==0:
                    dp[i][j]=True
                elif g==1:
                    if str[i]==str[j]:
                        dp[i][j]=True
                    else:
                        dp[i][j]=False
                else:
                    if str[i]==str[j] and dp[i+1][j-1]==True:
                        dp[i][j]=True
                    else:
                        dp[i][j]=False
        if dp[0][n-1]==True:
            return 0
        ans=[int(x) for x in range(n+1)]
        ans[0]=0
        ans[1]=0
        ans[2]=0
        if str[0]!=str[1]:
            ans[2]+=1
        for i in range(3,n+1):
            for j in range(i,0,-1):
                if dp[j-1][i-1]==True:
                    ans[i]=min(ans[i],ans[j-1]+1)
        # print(ans)
        return ans[n]
    
    str=input()
    ans1=PalindromicPartition(str)
    print(ans1)

if __name__=='__main__':
    main()
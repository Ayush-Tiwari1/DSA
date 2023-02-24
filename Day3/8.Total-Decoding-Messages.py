
def main():
    str=input()
    if len(str)==1:
        print(1)
        return
    dp=[0]*len(str)
    if str[0]=='0':
        print(0)
        return
    dp[0]=1
    if str[1]!='0':
        dp[1]=1
    if str[0:2]<='26':
        dp[1]+=1
    for i in range(2,len(str)):
        if str[i]=='0':
            if str[i-1]=='0':
                print(0)
                return
            if str[i-1]=='1' or str[i-1]=='2':
                dp[i]+=dp[i-2]
        else:
            if str[i-1]=='0':
                dp[i]+=dp[i-1]
            else:
                dp[i]+=dp[i-1]
                if str[i-1:i+1]<='26':
                    dp[i]+=dp[i-2]
    # print(dp)
    print(dp[len(str)-1])
    

if __name__=='__main__':
    main()
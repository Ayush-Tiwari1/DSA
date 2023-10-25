# Coin Change Problem
# Repeatation of Coins Allowed


def CoinChange2(indx,coins,sum,string,ans):

    if indx==len(coins):
        if sum==0:
            ans.append(string)
        return

    for j in range(sum//coins[indx],0,-1):
        temp=""
        for i in range(j):
            temp+=(str(coins[indx])+"-")
        CoinChange2(indx+1,coins,sum-coins[indx]*j,string+temp,ans)

    # Exclude
    CoinChange2(indx+1,coins,sum,string,ans)
        


def main():
    n=int(input())
    coins=list(map(int,input().split()))
    sum=int(input())
    ans=[]
    CoinChange2(0,coins,sum,"",ans)
    for combi in ans:
        print(combi)


if __name__=='__main__':
    main()
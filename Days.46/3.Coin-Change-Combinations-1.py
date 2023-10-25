# Coin Change Combination-1
# Include/ Exclude Concept
# Repeatation of Coins are not allowed

def CoinChange(indx,coins,sum,temp,ans):
    
    if sum<0:
        return
    if indx==len(coins):
        if sum==0:
            ans.append(temp[1:])
        return
    
    # Include
    CoinChange(indx+1,coins,sum-coins[indx],temp+"-"+str(coins[indx]),ans)
    
    # Exclude
    CoinChange(indx+1,coins,sum,temp,ans)
    
def main():
    n=int(input())
    coins=list(map(int,input().split()))
    sum=int(input())
    ans=[]
    CoinChange(0,coins,sum,"",ans)
    print('Coin Change Combinations are:')
    for combi in ans:
        print(combi)


if __name__=="__main__":
    main()



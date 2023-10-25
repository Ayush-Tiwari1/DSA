# Tug of War / Minimum Subset Sum Difference


def TugOfWar(indx,set1,set2,sum1,sum2,arr,minisum,ans):
    if indx==len(arr):
        if abs(sum1[0]-sum2[0])<minisum[0]:
            minisum[0]=abs(sum1[0]-sum2[0])
            ans[0]=set1[:]
            ans[1]=set2[:]
        return
    
    # Include in first set
    if len(set1)<(len(arr)+1)//2:
        set1.append(arr[indx])
        sum1[0]+=arr[indx]
        TugOfWar(indx+1,set1,set2,sum1,sum2,arr,minisum,ans)
        sum1[0]-=arr[indx]
        set1.pop()
    
    # Include in second set
    if len(set2)<(len(arr)+1)//2:
        set2.append(arr[indx])
        sum2[0]+=arr[indx]
        TugOfWar(indx+1,set1,set2,sum1,sum2,arr,minisum,ans)
        sum2[0]-=arr[indx]
        set2.pop()
    
    

def main():
    n=int(input())
    arr=list(map(int,input().split()))
    ans=[[],[]]
    minisum=[2**62]
    set1=[]
    set2=[]
    sum1=[0]
    sum2=[0]
    TugOfWar(0,set1,set2,sum1,sum2,arr,minisum,ans)
    print('Subset lists:',ans[0],ans[1])
    print('Minimum Sum:',minisum[0])
if __name__=='__main__':
    main()
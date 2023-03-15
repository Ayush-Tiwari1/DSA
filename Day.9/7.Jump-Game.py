


def main():
    def JumpGame(arr,n):
        if n==1:
            return 1
        if arr[0]==0:
            return 0
        maxReach=arr[0]
        jumps=0
        steps=arr[0]
        for i in range(1,n-1):
            steps-=1
            maxReach=max(maxReach,i+arr[i])
            if steps==0:
                jumps+=1
                steps=maxReach-i
                if steps==0:
                    return 0
        return 1
        
    n=int(input())
    arr=list(map(int,input().strip().split()))
    ans=JumpGame(arr,n)
    print(ans)

if __name__=='__main__':
    main()
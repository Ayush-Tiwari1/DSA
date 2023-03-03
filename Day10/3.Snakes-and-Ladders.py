
from collections import deque
def main():
    def SnakeLadder(n,arr):
        ladder=[-1]*31
        for i in range(0,2*n,2):
            ladder[arr[i]]=arr[i+1]
        # print(ladder)
        q=deque()
        q.append([1,0])
        ladder[1]=0
        while len(q)>0:
            front=q.popleft()
            if front[0]==30:
                return front[1]
            for i in range(1,7):
                indx=front[0]+i
                if indx<=30 and ladder[indx]!=0:
                    if ladder[indx] ==-1:
                        q.append([indx,front[1]+1])
                        ladder[indx]=0
                    else:
                        if ladder[indx]<indx:
                            ladder[indx]=0
                        else:
                            q.append([ladder[indx],front[1]+1])
                            ladder[ladder[indx]]=0
                            ladder[indx]=0
            # print(ladder)
        return -1
            
    n=int(input())
    arr=list(map(int,input().split()))
    ans=SnakeLadder(n,arr)
    print(ans)


if __name__=='__main__':
    main()
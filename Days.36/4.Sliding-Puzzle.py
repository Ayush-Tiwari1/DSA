# Sliding Puzzle 
'''
2x3---> Board
solve into: 
1 2 3
4 5 0
else: 
return -1
'''

from collections import deque

def SlidingPuzzle(brd):
    board=""
    for row in brd:
        for col in row:
            board+=str(col)
    dq=deque()
    dq.append(board)
    level=-1
    dict={}
    dict[board]=True
    moves=[[1,3],[0,2,4],[1,5],[0,4],[1,3,5],[2,4]]
    while dq:
        size=len(dq)
        level+=1
        for _ in range(size):
            board=dq.popleft()
            if board=="123450":
                return level
            indx=0
            while indx<6:
                if board[indx]=='0':
                    break
                else:
                    indx+=1
            for possible in moves[indx]:
                newboard=''
                for i in range(6):
                    if i==possible:
                        newboard+=board[indx]
                    elif i==indx:
                        newboard+=board[possible]
                    else:
                        newboard+=board[i]
                if newboard not in dict:
                    dq.append(newboard)
                    dict[newboard]=True
    
    return -1


def main():
    board=[]
    for i in range(2):
        board.append(list(map(int,input().split())))
    ans=SlidingPuzzle(board)
    print(ans)


if __name__=='__main__':
    main()
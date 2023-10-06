# N-Queen Problem

def isValid(row,col,chess):
    for j in range(0,col):
        if chess[row][j]==1:
            return False
    
    for i in range(0,row):
        if chess[i][col]==1:
            return False
    
    i=row-1
    j=col-1
    while i>=0 and j>=0:
        if chess[i][j]==1:
            return False
        i-=1
        j-=1
    
    i=row-1
    j=col+1
    while i>=0 and j<len(chess):
        if chess[i][j]==1:
            return False
        i-=1
        j+=1
    return True


def NQueen(row,chess,temp,ans,n):
    if row==n:
        ans.append(temp[:])
        return
    for j in range(n):
        if isValid(row,j,chess)==True:
            temp.append(j+1)
            chess[row][j]=1
            NQueen(row+1,chess,temp,ans,n)
            chess[row][j]=0
            temp.pop()

def main():
    n=int(input())
    ans=[]
    chess=[[0 for j in range(n)] for i in range(n)]
    temp=[]
    NQueen(0,chess,temp,ans,n)
    for position in ans:
        print(position)



if __name__=='__main__':
    main()
# Solve the Sudoku

def isValid(i,j,val,sudoku):
    row=(i//3)*3
    col=(j//3)*3
    for k in range(9):
        if sudoku[k][j]==val:
            return False
    for k in range(9):
        if sudoku[i][k]==val:
            return False
    
    for r in range(3):
        for c in range(3):
            if sudoku[r+row][c+col]==val:
                return False
    return True


def Sudoku(row,col,sudoku):
    if row==9:
        return True
    i=row
    j=col+1
    if col==8:
        i=row+1
        j=0
        
    if sudoku[row][col]!=0:
        return Sudoku(i,j,sudoku)
    else:
        for k in range(1,10):
            if isValid(row,col,k,sudoku):
                sudoku[row][col]=k
                flag=Sudoku(i,j,sudoku)
                if flag==True:
                    return True
                sudoku[row][col]=0
    


def main():
    sudoku=[]
    for i in range(9):
        sudoku.append(list(map(int,input().split())))
    ans=Sudoku(0,0,sudoku)
    if ans==True:
        for i in range(9):
            for j in range(9):
                print(sudoku[i][j],end=" ")
            print()




if __name__=='__main__':
    main()
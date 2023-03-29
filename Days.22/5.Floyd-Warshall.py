#All Pair Shortest Path

def FloydWarshall(matrix,n):
    #All pair shortest path via 1 2 3 4 ..... n Vertex
    #dist[1][3] via 2===> min(dist[1][3],dist[1][2]+dist[2][3])
    maxi=2**63
    for i in range(n):
        for j in range(n):
            if matrix[i][j]==-1:
                matrix[i][j]=maxi
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i==j:
                    matrix[i][j]=0
                elif i!=k and j!=k:
                    if matrix[i][k]!=maxi and matrix[k][j]!=maxi:
                        matrix[i][j]=min(matrix[i][j],matrix[i][k]+matrix[k][j])
    for i in range(n):
        for j in range(n):
            if matrix[i][j]==maxi:
                matrix[i][j]=-1

def main():
    n=int(input())
    matrix=[]
    for i in range(n):
        matrix.append(list(map(int,input().strip().split())))
    print(matrix)
    FloydWarshall(matrix,n)
    print('All Pairs Shortest Path are:')
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end=" ")
        print()


if __name__=='__main__':
    main()
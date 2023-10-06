# Get Stairs Path
# Jump ----> 1, 2, 3


def GetStairsPath(n):
    if n<0:
        return []
    if n==0:
        return [""]
    path1=GetStairsPath(n-1)    
    path2=GetStairsPath(n-2)
    path3=GetStairsPath(n-3)
    ans=[]
    for path in path1:
        ans.append("1"+path)
    for path in path2:
        ans.append("2"+path)
    for path in path3:
        ans.append("3"+path)
    return ans
    



def main():
    n=int(input())
    paths=GetStairsPath(n)
    for path in paths:
        print(path)

if __name__=='__main__':
    main()
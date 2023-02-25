
def main():
    def SecondElement(Pair):
        return Pair[1]
    def MaxLengthChain(Parr):
        max_length=1
        curr_length=1
        first=Parr[0][0]
        second=Parr[0][1]
        for i in range(1,len(Parr)):
            if Parr[i][0]>second:
                curr_length+=1
                first=Parr[i][0]
                second=Parr[i][1]
            max_length=max(max_length,curr_length)
        return max_length
    n=int(input())
    arr=[int(x) for x in input().split()]
    Parr=[]
    i=0
    while n*2>i:
        Parr.append([arr[i],arr[i+1]])
        i+=2
    # print('Original List:',Parr)
    # Parr.sort()
    # print('Ascending Order:',Parr)
    # Parr.sort(reverse=True)
    # print('Descending Order:',Parr)
    # Parr.sort(key=SecondElement)
    # print("User's Choice",Parr)
    
    Parr.sort(key=SecondElement)
    ans=MaxLengthChain(Parr)
    print(ans)
if __name__=='__main__':
    main()
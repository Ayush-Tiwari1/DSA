#Majority Element using Moore's Algorithm

def MajorityElement(n,arr):
    element=arr[0]
    count=1
    for i in range(1,n):
        if arr[i]==element:
            count+=1
        else:
            count-=1
        if count==0:
            element=arr[i]
            count=1
    
    count=0
    for i in range(n):
        if arr[i]==element:
            count+=1
    
    if count > n//2:
        return element
    return -1

def main():
    n=int(input())
    arr=list(map(int,input().split()))
    ans=MajorityElement(n,arr)
    if ans==-1:
        print('No Majority Element')
    else:
        print('Majority Element:',ans)


main()
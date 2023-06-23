#Merge Without Extra Space
#Gap Method is used

def Merge(n,m,arr1,arr2):
    gap=(n+m)
    while gap!=1:
        gap=(gap+1)//2
        i=0
        j=gap
        while j<(n+m):
            if i<n and j<n:
                if arr1[i]>arr1[j]:
                    arr1[i],arr1[j]= arr1[j], arr1[i]
            elif i<n:
                if arr1[i]>arr2[j%n]:
                    arr1[i],arr2[j%n]=arr2[j%n], arr1[i]
            else:
                if arr2[i%n]>arr2[j%n]:
                    arr2[i%n],arr2[j%n]=arr2[j%n],arr2[i%n]
            i+=1
            j+=1

def main():
    n=int(input())
    arr1=list(map(int,input().split()))
    m=int(input())
    arr2=list(map(int,input().split()))
    Merge(n,m,arr1,arr2)
    print(arr1)
    print(arr2)


main()
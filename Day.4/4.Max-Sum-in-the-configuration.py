
def max_sum(a,n):
    sum=0
    curr_val=0
    for i in range(n):
        sum+=a[i]
        curr_val+=(i*a[i])
    max_val=curr_val
    for i in range(1,n):
        next_val=curr_val-(sum-a[i-1])+a[i-1]*(n-1)
        curr_val=next_val
        max_val=max(max_val,curr_val)
    return max_val

    
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr,n))

# Largest Area Histogram using Stack
# Time Complexity   : O(n)
# Space Complexity  : O(n)


def LargestAreaHistogram(histogram,n):
    stack=[]
    
    #Next Smaller Left
    nsl=[-1 for i in range(n)]
    for i in range(n):
        while len(stack)>0 and histogram[i]<=histogram[stack[-1]]:
            stack.pop()
        if len(stack)==0:
            nsl[i]=-1
        else:
            nsl[i]=stack[-1]
        stack.append(i)
    
    while len(stack)>0:
        stack.pop()
    
    #Next Smaller Right
    nsr=[n for i in range(n)]
    for i in range(n-1,-1,-1):
        while len(stack)>0 and histogram[i]<=histogram[stack[-1]]:
            stack.pop()
        if len(stack)==0:
            nsr[i]=n
        else:
            nsr[i]=stack[-1]
        stack.append(i)
    maxarea=-2**63
    for i in range(n):
        maxarea=max(maxarea,(nsr[i]-nsl[i]-1)*histogram[i]);
    return maxarea

def main():
    n=int(input())
    histogram=list(map(int,input().split()))
    maxarea=LargestAreaHistogram(histogram,n)
    print(maxarea)



main()
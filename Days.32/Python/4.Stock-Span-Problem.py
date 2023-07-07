# Stock Span Problem


def StockSpan(prices,n):
    days=[1 for i in range(n)]
    stack=[]
    for i in range(0,n):
        while len(stack)>0 and prices[i]>=prices[stack[-1]]:
            stack.pop()
        if len(stack)==0:
            days[i]=i+1
        else:
            days[i]=i-stack[-1]
        stack.append(i)
    return days


def main():
    n=int(input())
    prices=list(map(int,input().split()))
    days=StockSpan(prices,n)
    for day in days:
        print(day,end=" ")
    print()

main()





def main():
    
    #O(n)--->TC
    #O(n)--->SC
    def LongestValidParentheses1(str):
        n=len(str)
        anslen=0
        stack=[]
        stack.append(-1)
        for i in range(n):
            if str[i]=='(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack)==0:
                    stack.append(i)
                else:
                    anslen=max(anslen,i-stack[-1])
        return anslen
    #O(n)--->TC
    #O(1)--->SC
    def LongestValidParentheses2(str):
        anslen=0
        left=0
        right=0
        n=len(str)
        for i in range(n):
            if str[i]=='(':
                left+=1
            else:
                right+=1
            if left==right:
                anslen=max(anslen,2*left)
            elif right>left:
                left=right=0
        
        left=right=0
        for i in range(n-1,-1,-1):
            if str[i]=='(':
                left+=1
            else:
                right+=1
            if left==right:
                anslen=max(anslen,2*left)
            elif left>right:
                left=right=0
        return anslen
        
    str=input()
    ans=LongestValidParentheses2(str)
    print(ans)

if __name__=='__main__':
    main()
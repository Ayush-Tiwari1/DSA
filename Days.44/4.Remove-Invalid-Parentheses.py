# Remove Invalid Parentheses

def CountInvalidParentheses(string):
    stack=[]
    for char in string:
        if char=='(':
            stack.append(char)
        elif char==')':
            if len(stack)==0 or stack[-1]==')':
                stack.append(char)
            else:
                stack.pop()
    return len(stack)

def RemoveInvalidParentheses(string,k,ans,dict):
    if string in dict:
        return
    if k==0:
        if CountInvalidParentheses(string)==0 and string not in dict:
            ans.append(string)
            dict[string]=True
        return
    dict[string]=True
    for i in range(len(string)):
        prefix=string[0:i]
        suffix=string[i+1:]
        RemoveInvalidParentheses(prefix+suffix,k-1,ans,dict)

def main():
    string=input()
    ans=[]
    k=CountInvalidParentheses(string)
    dict={}
    RemoveInvalidParentheses(string,k,ans,dict)
    for valid in ans:
        print(valid)

if __name__=="__main__":
    main()
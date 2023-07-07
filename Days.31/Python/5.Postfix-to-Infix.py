# Postfix ----> Infix


def PostfixtoInfix(str):
    n=len(str)
    stack=[]
    for i in range(0,n):
        if str[i]=='+' or str[i]=='-' or str[i]=='*' or str[i]=='/' or str[i]=='^':
            b=stack.pop()
            a=stack.pop()
            stack.append('('+a+str[i]+b+')')
        else:
            stack.append(str[i])
    return stack[-1]


def main():
    str=input()
    ans=PostfixtoInfix(str)
    print(ans)


main()


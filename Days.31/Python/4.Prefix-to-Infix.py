# Prefix ---> Infix

def PrefixtoInfix(str):
    stack=[]
    # Read Right to Left
    for i in range(len(str)-1,-1,-1):
        if str[i]=='+' or str[i]=='-' or str[i]=='*' or str[i]=='/' or str[i]=='^':
            a=stack.pop()
            b=stack.pop()
            stack.append('('+a+str[i]+b+')')
        else:
            stack.append(str[i])
    return stack[-1]
    


def main():
    str=input()
    ans=PrefixtoInfix(str)
    print(ans)



main()


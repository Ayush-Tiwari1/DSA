# Postfix ----> Prefix


def PostfixtoPrefix(str):
    op=[]
    for i in range(len(str)):
        if str[i]=='+' or str[i]=='-' or str[i]=='*' or str[i]=='/' or str[i]=='^':
            b=op.pop()
            a=op.pop()
            op.append(str[i]+a+b)
        else:
            op.append(str[i])
    return op[-1]
            

def main():
    str=input()
    ans=PostfixtoPrefix(str)
    print(ans)


main()


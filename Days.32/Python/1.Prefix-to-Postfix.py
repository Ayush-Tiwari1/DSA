# Prefix ----> Postfix


def PrefixtoPostfix(str):
    op=[]
    for i in range(len(str)-1,-1,-1):
        if str[i]=='+' or str[i]=='-' or str[i]=='*' or str[i]=='/' or str[i]=='^':
            a=op.pop()
            b=op.pop()
            op.append(a+b+str[i])
        else:
            op.append(str[i])
    
    return op[-1]
            


def main():
    str=input()
    ans=PrefixtoPostfix(str)
    print(ans)



main()


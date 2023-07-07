# Infix ----> Prefix

def Precedence(operator):
    if operator=='^':
        return 3
    elif operator=='*' or operator=='/':
        return 2
    elif operator=='+' or operator=='-':
        return 1
    return 0


def InfixtoPrefix(str):
    operand=[]
    operator=[]
    for i in range(len(str)):
        if str[i]=='+' or str[i]=='-' or str[i]=='*' or str[i]=='/' or str[i]=='^':
            while operator and Precedence(operator[-1])>=Precedence(str[i]):
                b=operand.pop()
                a=operand.pop()
                operand.append(operator[-1]+a+b)
                operator.pop()
            operator.append(str[i])
        elif str[i]=='(':
            operator.append(str[i])
        elif str[i]==')':
            while operator[-1]!='(':
                b=operand.pop()
                a=operand.pop()
                operand.append(operator[-1]+a+b)
                operator.pop()
            operator.pop()
        else:
            operand.append(str[i])
    while operator:
        b=operand.pop()
        a=operand.pop()
        operand.append(operator[-1]+a+b)
        operator.pop()
    return operand[-1]

def main():
    str=input()
    ans=InfixtoPrefix(str)
    print(ans)


main()


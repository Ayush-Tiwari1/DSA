# Infix ----> Postfix Conversion

def precedence(operator):
    if operator== '^':
        return 3
    elif operator=='*' or operator=='/':
        return 2
    elif operator=='+' or operator=='-':
        return 1
    return 0

def InfixtoPostfix(str):
    n=len(str)
    operands=[]
    operators=[]
    
    for i in range(n):
        if str[i]=='+' or str[i]=='-' or str[i]=='*' or str[i]=='/' or str[i]=='^':
            while len(operators)>0 and operators[-1]!='(' and precedence(str[i])<=precedence(operators[-1]):
                b=operands.pop()
                a=operands.pop()
                operands.append(a+b+operators[-1])
                operators.pop()
            operators.append(str[i])
            
        elif str[i]=='(':
            operators.append(str[i])
        elif str[i]==')':
            while len(operators)>0 and operators[-1]!='(':
                b=operands.pop()
                a=operands.pop()
                operands.append(a+b+operators[-1])
                operators.pop()
            operators.pop()
        else:
            operands.append(str[i])
        # print(operands)
        # print(operators)
    while len(operators)>0:
        b=operands.pop()
        a=operands.pop()
        operands.append(a+b+operators[-1])
        operators.pop()
    operators.append(str[i])
    return operands[-1]

def main():
    str=input()
    ans=InfixtoPostfix(str)
    print(ans)



main()


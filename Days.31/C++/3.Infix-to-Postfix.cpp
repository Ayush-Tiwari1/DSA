// Infix to Postfix Conversion


#include<iostream>
#include<string>
#include<vector>
#include<typeinfo>
using namespace std;

int Precedence(char Operator)
{
    if (Operator=='^')
    {
        return 3;
    }
    else if (Operator=='*' or Operator=='/')
    {
        return 2;
    }
    else if(Operator=='+' or Operator=='-')
    {
        return 1;
    }
    return 0;
}

template<typename T>
void Print(vector<T> v)
{
    for(int i=0; i<v.size(); i++)
    {
        cout<<v[i]<<" ";
    }
    cout<<"\n";
}

string InfixtoPostfix(string &str)
{
    int n=str.size();
    vector<string> operands;
    vector<char> operators;
    int size;
    string a,b,c;
    string temp;
    for(int i=0; i<n; i++)
    {
        if (str[i]=='(')
        {
            operators.push_back(str[i]);
        }
        else if(str[i]=='+' or str[i]=='-' or str[i]=='*' or str[i]=='/' or str[i]=='^')
        {
            while(!operators.empty() and operators.back()!='(' and Precedence(str[i])<=Precedence(operators.back()))
            {
                b=operands.back();
                operands.pop_back();
                a=operands.back();
                operands.pop_back();
                c=a+b+operators.back();
                operands.push_back(c);
                operators.pop_back();
            }
            operators.push_back(str[i]);
        }
        else if (str[i]==')')
        {
            while(!operators.empty() and operators.back()!='(')
            {
                b=operands.back();
                operands.pop_back();
                a=operands.back();
                operands.pop_back();
                c=a+b+operators.back();
                operands.push_back(c);
                operators.pop_back();
            }
            operators.pop_back();
        }
        else
        {
            temp=str[i];
            operands.push_back(temp);
        }
    }
    while (!operators.empty())
    {
        b=operands.back();
        operands.pop_back();
        a=operands.back();
        operands.pop_back();
        c=a+b+operators.back();
        operators.pop_back();
        operands.push_back(c);
    }
    return operands.back();
}

int main()
{
    string str;
    cin>>str;
    string ans=InfixtoPostfix(str);
    cout<<ans<<"\n";
    return 0;
}
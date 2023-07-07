// Infix ----> Prefix

#include<iostream>
#include<vector>
using namespace std;

int Precedence(char Operator)
{
    if (Operator=='^')
    {
        return 3;
    }
    else if(Operator=='*' or Operator=='/')
    {
        return 2;
    }
    else if(Operator=='+' or Operator=='-')
    {
        return 1;
    }
    else{
        return 0;
    }
}

string InfixtoPrefix(string &str)
{
    vector<string> Operand;
    vector<char> Operator;
    string a,b,c,temp;
    for(int i=0; i<str.size(); i++)
    {
        if (str[i]=='(')
        {
            Operator.push_back(str[i]);
        }
        else if(str[i]==')')
        {
            while (!Operator.empty() and Operator.back()!='(')
            {
                b=Operand.back();
                Operand.pop_back();
                a=Operand.back();
                Operand.pop_back();
                c=Operator.back()+a+b;
                Operand.push_back(c);
                Operator.pop_back();
            }
            Operator.pop_back();
        }
        else if(str[i]=='+' or str[i]=='-' or str[i]=='*' or str[i]=='/' or str[i]=='^')
        {
            while (!Operator.empty() and Operator.back()!='(' and Precedence(str[i])<=Precedence(Operator.back()))    
            {
                b=Operand.back();
                Operand.pop_back();
                a=Operand.back();
                Operand.pop_back();
                c=Operator.back()+a+b;
                Operand.push_back(c);
                Operator.pop_back();
            }
            Operator.push_back(str[i]);
        }
        else
        {
            temp=str[i];
            Operand.push_back(temp);
        }
    }
    while (!Operator.empty())
    {
        b=Operand.back();
        Operand.pop_back();
        a=Operand.back();
        Operand.pop_back();
        c=Operator.back()+a+b;
        Operand.push_back(c);
        Operator.pop_back();
    }
    return Operand.back();
}


int main()
{
    string str;
    cin>>str;
    string ans=InfixtoPrefix(str);
    cout<<ans<<"\n";
    return 0;
}
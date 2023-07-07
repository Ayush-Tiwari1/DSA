// Postfix ----> Prefix
#include<iostream>
#include<vector>
using namespace std;

string PostfixtoPrefix(string &str)
{
    vector<string> op;
    string a,b,temp;
    for(int i=0; i<str.size(); i++)
    {
        if (str[i]=='+' or str[i]=='-' or str[i]=='*' or str[i]=='/' or str[i]=='^')
        {
            b=op.back();
            op.pop_back();
            a=op.back();
            op.pop_back();
            op.push_back(str[i]+a+b);
        }
        else
        {
            temp=str[i];
            op.push_back(temp);
        }
    }
    return op.back();
}

int main()
{
    string str;
    cin>>str;
    string ans=PostfixtoPrefix(str);
    cout<<ans<<"\n";
    return 0;
}
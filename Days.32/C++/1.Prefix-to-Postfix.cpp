// Prefix ----> Postfix
#include<iostream>
#include<vector>
using namespace std;


string PostfixtoPrefix(string &str)
{
    vector<string> op;
    string a,b,temp;
    for (int i=str.size()-1; i>=0; i--)
    {
        if (str[i]=='+' or str[i]=='-' or str[i]=='*' or str[i]=='/' or str[i]=='^')
        {
            a=op.back();
            op.pop_back();
            b=op.back();
            op.pop_back();
            op.push_back(a+b+str[i]);
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
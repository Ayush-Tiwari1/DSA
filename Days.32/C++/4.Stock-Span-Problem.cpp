// Stock Span Problem 

#include<iostream>
#include<vector>
#include<stack>
using namespace std;


vector<int> StockSpan(vector<int> &prices,int &n)
{
    vector<int> days(n,1);
    stack<int> stack;
    for (int i=0; i<n; i++)
    {
        while (!stack.empty() and prices[i]>=prices[stack.top()])
        {
            stack.pop();
        }
        if(stack.empty())
        {
            days[i]=i+1;
        }
        else
        {
            days[i]=i-stack.top();
        }
        stack.push(i);
    }
    return days;
}


int main()
{
    int n;
    cin>>n;
    vector<int> prices(n);
    for (int i=0; i<n; i++)
    {
        cin>>prices[i];
    }
    vector<int> days=StockSpan(prices,n);
    for(int i=0; i<n; i++)
    {
        cout<<days[i]<<" ";
    }
    cout<<"\n";
    return 0;
}
// Largest Area Histogram using Stack
// Time Complexity  : O(n)
// Space Complexity : O(n)

#include<iostream>
#include<vector>
#include<climits>
#include<stack>
using namespace std;


int LargestAreaHistogram(vector<int> &histogram,int &n)
{
    stack<int> st;
    vector<int> nsl(n,-1);
    vector<int> nsr(n,n);
    
    // Next Smaller Right
    for (int i=n-1; i>=0; i--)
    {
        while (!st.empty() and histogram[i]<=histogram[st.top()])
        {
            st.pop();
        }
        if (st.empty())
        {
            nsr[i]=n;
        }
        else
        {
            nsr[i]=st.top();
        }
        st.push(i);
    }
    
    while (!st.empty())
    {
        st.pop();
    }
    
    // Next Smaller Left
    for(int i=0; i<n; i++)
    {
        while (!st.empty() and histogram[i]<=histogram[st.top()])
        {
            st.pop();
        }
        if(st.empty())
        {
            nsl[i]=-1;
        }
        else
        {
            nsl[i]=st.top();
        }
        st.push(i);
    }
    
    int maxarea=INT_MIN;
    for(int i=0; i<n; i++)
    {
        maxarea=max(maxarea,(nsr[i]-nsl[i]-1)*histogram[i]);
    }
    return maxarea;
}


int main()
{
    int n;
    cin>>n;
    vector<int> v(n);
    for(int i=0; i<n; i++)
    {
        cin>>v[i];
    }
    int maxarea=LargestAreaHistogram(v,n);
    cout<<maxarea<<"\n";
    return 0;
}
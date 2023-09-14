// Median in a Running Stream

#include<iostream>
#include<vector>
#include<queue>
using namespace std;

class Solution
{
    priority_queue<int,vector<int> > maxheap;
    priority_queue<int,vector<int>,greater<int> > minheap;
    public:
    void balanceHeaps()
    {
        int val;
        if(minheap.size()>maxheap.size())
        {
            val=minheap.top();
            minheap.pop();
            maxheap.push(val);
        }
        else if(maxheap.size()>minheap.size()+1)
        {
            val=maxheap.top();
            maxheap.pop();
            minheap.push(val);
        }
    }
    void insertHeap(int x)
    {
        if(maxheap.size()==0 or x<maxheap.top())
        {
            maxheap.push(x);
        }
        else
        {
            minheap.push(x);
        }
        balanceHeaps();
    }
    double getMedian()
    {
        if(maxheap.size()>minheap.size())
        {
            return maxheap.top();
        }
        else
        {
            return (maxheap.top()+minheap.top())/2.0;
        }
    }
};

int main()
{
    int n;
    cin>>n;
    int x;
    Solution solution;
    for(int i=0; i<n; i++)
    {
        cin>>x;
        solution.insertHeap(x);
        cout<<"Median: "<<solution.getMedian()<<"\n";
    }
    return 0;
}
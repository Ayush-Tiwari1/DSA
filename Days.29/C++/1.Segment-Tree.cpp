#include<iostream>
#include<climits>
#include<vector>
using namespace std;


int BuildTree(int indx,int low,int high,vector<int> &arr,vector<int> &segtree)
{
   if(low==high)
   {
       segtree[indx]=arr[low];
       return segtree[indx];
   }
   int mid=(low+(high-low)/2);
   int left=BuildTree(2*indx+1,low,mid,arr,segtree);
   int right=BuildTree(2*indx+2,mid+1,high,arr,segtree);
   segtree[indx]=min(left,right);
   return segtree[indx];
}

int Find(int indx,int low,int high,int l,int r,vector<int> &segtree)
{
    // No Overlap
    if(high<l or low>r)
    {
      return INT_MAX;  
    }
    // Complete Overlap
    else if(low>=l and high<=r)
    {
        return segtree[indx];
    }
    // Partial Overlap
    else
    {
        int mid=(low+(high-low)/2);
        int left=Find(2*indx+1,low,mid,l,r,segtree);
        int right=Find(2*indx+2,mid+1,high,l,r,segtree);
        segtree[indx]=min(left,right);
        return segtree[indx];
    }
}

int Update(int indx,int low,int high, int i ,int val,vector<int> &segtree)
{
    if(high<i or low>i)
    {
        return segtree[indx];
    }
    if(low==high)
    {
        segtree[indx]=val;
        return segtree[indx];
    }
    int mid=(low+(high-low)/2);
    int left=Update(2*indx+1,low,mid,i,val,segtree);
    int right=Update(2*indx+2,mid+1,high,i,val,segtree);
    segtree[indx]=min(left,right);
    return segtree[indx];
}

int main()
{
    int n;
    cin>>n;
    vector<int> arr(n);
    for(int i=0; i<n; i++)
    {
        cin>>arr[i];
    }
    vector<int> segtree(4*n,-1);
    BuildTree(0,0,n-1,arr,segtree);
    // for(int val:segtree)
    // {
    //     cout<<val<<" ";
    // }
    int q;
    cin>>q;
    string query;
    int l,r;
    for(int i=0; i<q; i++)
    {
        cin>>query>>l>>r;
        if(query=="m")
        {
            int min=Find(0,0,n-1,l,r,segtree);
            cout<<query<<" ("<<l<<", "<<r<<") Min:\t"<<min<<"\n";
        }
        else if (query=="u")
        {
            Update(0,0,n-1,l,r,segtree);
            cout<<query<<" ("<<l<<", "<<r<<") Update:\t"<<"Update Successfully\n";
        }
    }
    return 0;
}
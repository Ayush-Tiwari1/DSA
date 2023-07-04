// Quick Sort using Haore's Partition

// Time Complexity:
// O(n*n)   ----> Worst Case
// O(nlogn) ----> Best Case and Average Case

#include<iostream>
#include<vector>
using namespace std;


int Partition(vector<int> &arr,int low,int high)
{
    int pivot=low;
    int i=low;
    int j=low+1;
    while (j<=high)
    {
        if (arr[j]<=arr[pivot])
        {
            i+=1;
            swap(arr[i],arr[j]);
        }
        j+=1;
    }
    swap(arr[i],arr[pivot]);
    return i;
}


void QuickSort(vector<int> &arr,int low,int high)
{
    if (low<high)
    {
        int m=Partition(arr,low,high);
        QuickSort(arr,low,m-1);
        QuickSort(arr,m+1,high);
    }
}


int main()
{
    int n;
    cin>>n;
    vector<int> arr(n);
    for (int i=0; i<n; i++)
    {
        cin>>arr[i];
    }
    QuickSort(arr,0,n-1);
    for(int i=0; i<n; i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<"\n";
    return 0;
}



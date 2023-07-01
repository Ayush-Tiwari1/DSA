/// Heap Implementation

#include<iostream>
#include<vector>

using namespace std;

template <typename T>
class Heap
{
    private:
        vector<T> heap;
    public:
        int size()
        {
            return heap.size();
        }
        bool isempty()
        {
            if(size()==0)
            {
                return true;
            }
            return false;
        }
        
        void Swap(int i,int j)
        {
            int temp;
            temp=heap[i];
            heap[i]=heap[j];
            heap[j]=temp;
        }
        
        void heapifyUp(int indx)
        {
            int smallest=indx;
            int left=2*indx+1;
            int right=2*indx+2;
            int n=size();
            if(left<n and heap[left]<heap[smallest])
            {
                smallest=left;
            }
            if(right<n and heap[right]<heap[smallest])
            {
                smallest=right;
            }
            if(smallest!=indx)
            {
                Swap(smallest,indx);
                heapifyUp(smallest);
            }
        }
        
        void heapifyDown(int i)
        {
            int par=(i-1)/2;
            while(par>=0 and heap[par]>heap[i])
            {
                Swap(par,i);
                i=par;
                par=(i-1)/2;
            }
        }
        
        void PrintHeap()
        {
            for(auto h:heap)
            {
                cout<<h<<" ";
            }
            cout<<"\n";
        }
        
       void push(int val)
       {
           heap.push_back(val);
           heapifyDown(heap.size()-1);
       }
       int pop()
       {
           if(isempty()==true)
           {
               cout<<"Heap is Empty\n";
               return -1;
           }
           Swap(0,heap.size()-1);
           int val=heap[heap.size()-1];
           heap.pop_back();
           heapifyUp(0);
           return val;
       }
       int peek()
       {
           if(isempty()==true)
           {
               cout<<"Heap is Empty\n";
               return -1;
           }
           return heap[0];
       }
        
};



int main()
{
    Heap<int> heap;
    int val;
    while(true)
    {
        cout<<"1.Push\n";
        cout<<"2.Pop\n";
        cout<<"3.Size\n";
        cout<<"4.Empty\n";
        cout<<"5.Peek\n";
        cout<<"6.Print Heap\n";
        cout<<"7.Exit\n";
        cout<<"Enter Your Choice:\t";
        int choice;
        cin>>choice;
        if(choice==1)
        {
            cout<<"Enter a Value:\t";
            cin>>val;
            heap.push(val);
        }
        else if(choice==2)
        {
            val=heap.pop();
            if(val!=-1)
            {
               cout<<"Pop Value:\t"<<val<<"\n"; 
            }
        }
        else if(choice==3)
        {
            cout<<"Heap Size:\t"<<heap.size()<<"\n";
        }
        else if(choice==4)
        {
            if(heap.isempty())
            {
                cout<<"Heap is Empty\n";
            }
            else
            {
                cout<<"Heap is Not Empty\n";
            }
        }
        else if(choice==5)
        {
            val=heap.peek();
            if(val!=-1)
            {
                cout<<"Peek Element:\t"<<val<<"\n";
            }
        }
        else if(choice==6)
        {
            heap.PrintHeap();
        }
        else if(choice==7)
        {
            exit(0);
        }
        else
        {
            cout<<"Invalid Choice\n";
        }
    }
    return 0;
}

// Doubly Linked List
#include<iostream>
using namespace std;
class Node
{
    public:
    int val;
    Node *prev;
    Node *next;
    Node(int val)
    {
        this->val=val;
        this->prev=this->next=NULL;
    }
};

class DLL
{
    private:
    Node *head,*tail;
    public:
    DLL()
    {
        head=tail=NULL;
    }
    int size();
    void InsertBegin(int);
    void InsertEnd(int);
    void InsertPosition(int,int);
    int DeleteBegin();
    int DeleteEnd();
    int DeletePosition(int);
    int Middle();
    void PrintDLL();
};

int DLL::size()
{
    int sz=0;
    Node *temp=head;
    while(temp!=NULL)
    {
        sz+=1;
        temp=temp->next;
    }
    return sz;
}

void DLL::InsertBegin(int val)
{
    if(head==NULL)
    {
        head=tail=new Node(val);
    }
    else
    {
        Node *temp=new Node(val);
        temp->next=head;
        head->prev=temp;
        head=temp;
    }
}

void DLL::InsertEnd(int val)
{
    if(head==NULL)
    {
        head=tail=new Node(val);
    }
    else
    {
        Node *temp=new Node(val);
        tail->next=temp;
        temp->prev=tail;
        tail=temp;
    }
}

void DLL::InsertPosition(int val,int pos)
{
    int n=size();
    if(pos<0 or pos>n)
    {
        cout<<"Index Out of Bound\n";
    }
    else
    {
        if(pos==0)
        {
            InsertBegin(val);
        }
        else if (pos==n)
        {
             InsertEnd(val);
        }
        else
        {
            Node *curr=head;
            int i=1;
            while (i!=pos)
            {
                i+=1;
                curr=curr->next;
            }
            Node *temp=new Node(val);
            temp->next=curr->next;
            if (curr->next!=NULL)
            {
                curr->next->prev=temp;
            }
            curr->next=temp;
            temp->prev=curr;
        }
    }
}

int DLL::DeleteBegin()
{
    if(head==NULL)
    {
        return -1;
    }
    else if (head->next==NULL)
    {
        int val=head->val;
        Node *temp=head;
        head=head->next;
        tail=tail->next;
        delete temp;
        return val;
    }
    else
    {
        int val=head->val;
        Node *temp=head;
        head=head->next;
        head->prev=NULL;
        delete temp;
        return val;
    }
}

int DLL::DeleteEnd()
{
    if (head==NULL)
    {
        return -1;
    }
    else if (head->next==NULL)
    {
        int val=head->val;
        Node *temp=head;
        head=head->next;
        tail=tail->next;
        head->prev=NULL;
        tail->prev=NULL;
        delete temp;
        return val;
    }
    else
    {
        Node *temp=tail;
        int val=tail->val;
        tail=tail->prev;
        tail->next=NULL;
        delete temp;
        return val;
    }
}

int DLL::DeletePosition(int pos)
{
    int n=size();
    if(pos<0 or pos>n)
    {
        return -1;
    }
    else
    {
        if(head==NULL)
        {
            return -1;
        }
        else if(head->next==NULL)
        {
            int val;
            val=head->val;
            Node *temp=head;
            head=head->next;
            tail=tail->next;
            delete temp;
            return val;
        }
        else
        {
            Node *curr=head;
            if (pos==1)
            {
                return DeleteBegin();
            }
            else if (pos==n)
            {
                return DeleteEnd();
            }
            else
            {
                int i=1;
                while (i!=pos)
                {
                    i+=1;
                    curr=curr->next;
                }
            
                int val=curr->val;
                curr->prev->next=curr->next;
                curr->next->prev=curr->prev;
                delete curr;
                return val;
            }
        }
    }
}

int DLL::Middle()
{
    Node *slow,*fast;
    slow=fast=head;
    
    if(slow==NULL)
    {
        return -1;
    }

    while(fast!=NULL and fast->next!=NULL)
    {
        slow=slow->next;
        fast=fast->next->next;
    }
    return slow->val;
}

void DLL::PrintDLL()
{
    Node *curr=head;
    if(curr==NULL)
    {
        cout<<"Doubly Linked List is Empty\n";
    }
    else
    {
        while(curr!=NULL)
        {
            cout<<curr->val<<" ";
            curr=curr->next;
        }
        cout<<"\n";
    }
}

int main()
{
    int choice,val,pos;
    DLL *dll=new DLL();
    while(true)
    {
        cout<<"1.Insert at the Begin\n";
        cout<<"2.Insert at the End\n";
        cout<<"3.Insert at the Given Index\n";
        cout<<"4.Delete at the Begin\n";
        cout<<"5.Delete at the End\n";
        cout<<"6.Delete at the Given Index\n";
        cout<<"7.Size\n";
        cout<<"8.Middle\n";
        cout<<"9.Print Doubly Linked List\n";
        cout<<"10.Exit\n";
        cout<<"Enter Your Choice\t";
        cin>>choice;
        if(choice==1)
        {
            cout<<"Enter a Value: ";
            cin>>val;
            dll->InsertBegin(val);
        }
        else if (choice==2)
        {
            cout<<"Enter a Value: ";
            cin>>val;
            dll->InsertEnd(val);
        }
        else if(choice==3)
        {
            cout<<"Enter a Value: ";
            cin>>val;
            cout<<"Enter a Position: ";
            cin>>pos;
            dll->InsertPosition(val,pos);
        }
        else if(choice==4)
        {
            val=dll->DeleteBegin();
            if(val==-1)
            {
                cout<<"Doubly Linked List is Empty\n";
            }
            else
            {
                cout<<"Deleted Value: "<<val<<"\n";
            }
        }
        else if(choice==5)
        {
            val=dll->DeleteEnd();
            if(val==-1)
            {
                cout<<"Doubly Linked List is Empty\n";
            }
            else
            {
                cout<<"Deleted Value: "<<val<<"\n";
            }
        }
        else if(choice==6)
        {
            cout<<"Enter a Position: ";
            cin>>pos;
            val=dll->DeletePosition(pos);
            if(val==-1)
            {
                cout<<"Index Out of Bound\n";
            }
            else
            {
                cout<<"Deleted Value at Position "<<pos<<" : "<<val<<"\n";
            }
        }
        else if(choice==7)
        {
            cout<<"Size: "<<dll->size()<<"\n";
        }
        else if(choice==8)
        {
            val=dll->Middle();
            if (val==-1)
            {
                cout<<"Doubly Linked List is Empty\n";
            }
            else
            {
                cout<<"Middle: "<<val<<"\n";
            }
        }
        else if(choice==9)
        {
            dll->PrintDLL();
        }
        else if(choice==10)
        {
            break;
        }
        else
        {
            cout<<"Invalid Choice\n";
        }
    }
    return 0;
}
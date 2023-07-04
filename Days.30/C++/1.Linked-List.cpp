#include<iostream>
#include<vector>

using namespace std;


class Node
{
    public:
    int val;
    Node *next;
    Node(int val)
    {
        this->val=val;
        this->next=NULL;
    }
};

class LinkedList
{
    public:
    Node *head;
    Node *tail;
    LinkedList()
    {
        head=NULL;
        tail=NULL;
    }
    int size()
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
    void InsertBegin(int val)
    {
        if(head==NULL)
        {
            head=tail=new Node(val);
        }
        else
        {
            Node *temp=new Node(val);
            temp->next=head;
            head=temp;
        }
    }

    void InsertEnd(int val)
    {
        if(head==NULL)
        {
            head=tail=new Node(val);
        }
        else
        {
            tail->next=new Node(val);
            tail=tail->next;
        }
    }

    void InsertPosition(int val,int pos)
    {
        int n=size();
        if(pos<0 or pos>n+1)
        {
            cout<<"Index Out of Bound\n";
        }
        else
        {
            if(pos==1)
            {
                InsertBegin(val);
            }
            else if (pos==n+1)
            {
                InsertEnd(val);
            }
            else
            {
                Node *prev,*curr;
                prev=NULL;
                curr=head;
                int i=1;
                while(i!=pos)
                {
                    prev=curr;
                    curr=curr->next;
                    i+=1;
                }
                Node *temp=new Node(val);
                temp->next=curr;
                prev->next=temp;
            }
        }

    }

    int DeleteBegin()
    {
        if(head==NULL)
        {
            return -1;
        }
        else{
            int val=head->val;
            Node *temp=head->next;
            delete head;
            head=temp;
            return val;
        }
    }

    int DeleteEnd()
    {
        if(head==NULL)
        {
            return -1;
        }
        else if(head->next==NULL)
        {
            int val=head->val;
            Node *temp=head;
            head=head->next;
            delete temp;
            return val;
        }
        else{
            Node *curr,*prev;
            prev=NULL;
            curr=head;
            while(curr->next!=NULL)
            {
                prev=curr;
                curr=curr->next;
            }
            int val=curr->val;
            prev->next=NULL;
            delete curr;
            return val;
        }
    }

    int DeletePosition(int pos)
    {
        int n=size();
        if (pos<0 or pos>n)
        {
            return -1;
        }
        if(pos==1)
        {
            return DeleteBegin();
        }
        else if(pos==n)
        {
            return DeleteEnd();
        }
        else{
            Node *curr,*prev;
            curr=head;
            prev=NULL;
            int i=1;
            while(i!=pos)
            {
                prev=curr;
                curr=curr->next;
            }
            int val;
            val=curr->val;
            prev->next=curr->next;
            delete curr;
            return val;
        }
    }

    void print()
    {
        Node *temp=head;
        while(temp!=NULL)
        {
            cout<<temp->val<<" ";
            temp=temp->next;
        }
        cout<<"\n";
    }
};


int main()
{
    LinkedList *linkedlist=new LinkedList();
    int choice,val,pos;
    while(true)
    {
        cout<<"1.Insert at the Beginning\n";
        cout<<"2.Insert at the End\n";
        cout<<"3.Insert at Given Position\n";
        cout<<"4.Delete at the Beginning\n";
        cout<<"5.Delete at the End\n";
        cout<<"6.Delete at Given Position\n";
        cout<<"7.Size\n";
        cout<<"8.Print List\n";
        cout<<"9.Exit\n";
        cout<<"Enter Your Choice:\t";
        cin>>choice;
        if(choice==1)
        {
            cout<<"Enter a Value:\t";
            cin>>val;
            linkedlist->InsertBegin(val);
        }
        else if(choice==2)
        {
            cout<<"Enter a Value:\t";
            cin>>val;
            linkedlist->InsertEnd(val);
        }
        else if(choice==3)
        {
            cout<<"Enter a Value:\t";
            cin>>val;
            cout<<"Enter a Position:\t";
            cin>>pos;
            linkedlist->InsertPosition(val,pos);
        }
        else if(choice==4)
        {
            val=linkedlist->DeleteBegin();
            if (val==-1)
            {
                cout<<"List is Empty\n";
            }
            else{
                cout<<"Deleted Value:\t"<<val<<"\n";
            }
        }
        else if(choice==5)
        {
            val=linkedlist->DeleteEnd();
            if(val==-1)
            {
                cout<<"List is Empty\n";
            }
            else{
                cout<<"Deleted Value:\t"<<val<<"\n";
            }
        }
        else if(choice==6)
        {
            cout<<"Enter a Position:\t";
            cin>>pos;
            val=linkedlist->DeletePosition(pos);
            if(val==-1)
            {
                cout<<"Index Out of Bound\n";
            }
            else
            {
                cout<<"Deleted Value at "<<pos<<": "<<val<<"\n";
            }
        }
        else if(choice==7)
        {
            cout<<"Size:\t"<<linkedlist->size()<<"\n";
        }
        else if(choice==8)
        {
            linkedlist->print();
        }
        else if(choice==9)
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


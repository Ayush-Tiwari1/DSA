// Reverse Doubly Linked List in a group of size k

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
        this->prev=this->next=nullptr;
    }
};

class DLL
{
    Node *head,*tail;
    public:
    DLL()
    {
        head=tail=nullptr;
    }
    void Insert(int val)
    {
        Node *temp=new Node(val);
        if (head==nullptr)
        {
            head=tail=temp;
        }
        else
        {
            tail->next=temp;
            temp->prev=tail;
            tail=temp;
        }
    }

    void Reverse(int k)
    {
        Node *oh,*ot,*th,*tt,*curr,*next;
        oh=ot=th=tt=next=nullptr;
        curr=head;
        int count=0;
        while (curr!=nullptr)
        {
            next=curr->next;
            if(count==k)
            {
                if (oh==nullptr)
                {
                    oh=th;
                    ot=tt;
                }
                else
                {
                    ot->next=th;
                    th->prev=ot;
                    ot=tt;
                }
                count=0;
                th=tt=nullptr;
            }
            else
            {
                if(th==nullptr)
                {
                    curr->prev=curr->next=nullptr;
                    th=tt=curr;
                }
                else
                {
                    curr->next=th;
                    th->prev=curr;
                    curr->prev=nullptr;
                    th=curr;
                }
                count+=1;
                curr=next;
            }
        }
        if(th!=nullptr)
        {
            ot->next=th;
            th->prev=ot;
            ot=tt;
        }
        head=oh;
        tail=ot;
    }

    void printHead()
    {
        Node *curr=head;
        while (curr!=nullptr)
        {
            cout<<curr->val<<" ";
            curr=curr->next;
        }
        cout<<"\n";
    }
    void printTail()
    {
        Node *curr=tail;
        while (curr!=nullptr)
        {
            cout<<curr->val<<" ";
            curr=curr->prev;
        }
        cout<<"\n";
    }
};

void BuildDLL(DLL *&dll,string &str)
{

    string temp="";
    for(int i=0; i<str.size(); i++)
    {
        if(str[i]==' ')
        {
            dll->Insert(stoi(temp));
            temp="";
        }
        else{
            temp+=str[i];
        }
    }
    dll->Insert(stoi(temp));
}

int main()
{
    string str;
    getline(cin,str);
    int k;
    cin>>k;
    DLL *dll=new DLL();
    BuildDLL(dll,str);
    dll->printHead();
    dll->printTail();
    dll->Reverse(k);
    dll->printHead();
    dll->printTail();
    return 0;
}
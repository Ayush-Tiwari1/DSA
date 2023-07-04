#include<iostream>
#include<vector>
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

class DoublyLinkedList
{
    public:
    Node *head,*tail;
    DoublyLinkedList()
    {
        head=NULL;
        tail=NULL;
    }
    void InsertEnd(int val)
    {
        Node *temp=new Node(val);
        if (head==NULL)
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
    int DeleteEnd()
    {
        if (head==NULL)
        {
            return -1;
        }
        else if (head->next==NULL)
        {
            Node *temp=head;
            int val=temp->val;
            head=head->next;
            tail=tail->next;
            delete temp;
            return val;
        }
        else
        {
            Node *temp=head;
            while(temp->next!=tail)
            {
                temp=temp->next;
            }
            int val;
            val=tail->val;
            Node *t=tail;
            tail->prev=NULL;
            temp->next=NULL;
            tail=temp;
            delete t;
            return val;
        }
    }
    void printDLL()
    {
        Node *curr=head;
        while (curr!=NULL)
        {
            cout<<curr->val<<" ";
            curr=curr->next;
        }
        cout<<"\n";
    }
    
};

vector<Node*> Split(Node *head)
{
    Node *slow,*fast;
    slow=fast=head;
    while(fast->next!=NULL and fast->next->next!=NULL)
    {
        slow=slow->next;
        fast=fast->next->next;
    }
    Node *head1,*head2;
    head1=head;
    head2=slow->next;
    slow->next=NULL;
    vector<Node*> ans;
    ans.push_back(head1);
    ans.push_back(head2);
    return ans;
}

Node* Merge(Node *head1, Node *head2)
{
    Node *head=new Node(-1);
    Node *temp=head;
    while (head1!=NULL and head2!=NULL)
    {
        if( head1->val<head2->val)
        {
            temp->next=head1;
            head1->prev=temp;
            head1=head1->next;
        }
        else
        {
            temp->next=head2;
            head2->prev=temp;
            head2=head2->next;
        }
        temp=temp->next;
    }
    if(head1!=NULL)
    {
        temp->next=head1;
        head1->prev=temp;
    }
    if(head2!=NULL)
    {
        temp->next=head2;
        head2->prev=temp;
    }
    head=head->next;
    head->prev=NULL;
    return head;
}

Node* MergeSort(Node *head)
{
    vector<Node*> h=Split(head);
    Node *head1,*head2,*h1,*h2;
    head1=h[0];
    head2=h[1];
    if (head2==NULL)
    {
        return head1;
    }
    h1=MergeSort(head1);
    h2=MergeSort(head2);
    return Merge(h1,h2);
}

int main()
{
    int n;
    cin>>n;
    DoublyLinkedList *dll= new DoublyLinkedList();
    int val;
    for (int i=0; i<n; i++)
    {
        cin>>val;
        dll->InsertEnd(val);
    }
    cout<<"Before Merge Sort:\n";
    dll->printDLL();
    dll->head=MergeSort(dll->head);
    cout<<"After Merge Sort:\n";
    dll->printDLL();
    return 0;
}



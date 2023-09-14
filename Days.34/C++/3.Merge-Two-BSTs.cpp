// Merge Two BST

/*
Algorithm:
1. Convert Two BST ----> DLL
2. Merge Two DLL
3. Convert DLL ---> BST 
*/

#include<iostream>
#include<queue>
#include<string>
using namespace std;

class Node
{
    public:
    int val;
    Node *left;
    Node *right;
    Node(int val)
    {
        this->val=val;
        this->left=this->right=nullptr;
    }
};


vector<string> Split(string &str)
{
    vector<string> nodes;
    string temp="";
    for(int i=0 ;i<str.size(); i++)
    {
        if(str[i]==' ')
        {
            nodes.push_back(temp);
            temp="";
        }
        else
        {
            temp+=str[i];
        }
    }
    nodes.push_back(temp);
    return nodes;
}

Node* BuildTree(vector<string> &nodes)
{
    int n=nodes.size();
    if(n==0 or nodes[0]=="N")
    {
        return nullptr;
    }
    Node *root=new Node(stoi(nodes[0]));
    int i=1;
    queue<Node*> q;
    Node *curr;
    q.push(root);
    while (!q.empty() and i<n)
    {
        curr=q.front();
        q.pop();
        if (nodes[i]!="N")
        {
            curr->left=new Node(stoi(nodes[i]));
            q.push(curr->left);
        }
        i++;
        if (i>=n)
        {
            break;
        }
        if(nodes[i]!="N")
        {
            curr->right=new Node(stoi(nodes[i]));
            q.push(curr->right);
        }
        i++;
    }
    return root;
}

void Inorder(Node *root)
{
    if(root==nullptr)
    {
        return;
    }
    Inorder(root->left);
    cout<<root->val<<" ";
    Inorder(root->right);
}

void PrintDLL(Node *head)
{
    Node *curr=head;
    Node *tail=nullptr;
    cout<<"Left to Right:\n";
    while (curr!=nullptr)
    {
        cout<<curr->val<<" ";
        tail=curr;
        curr=curr->right;
    }
    cout<<"\nRight to Left:\n";
    while (tail!=nullptr)
    {
        cout<<tail->val<<" ";
        tail=tail->left;
    }
    cout<<"\n";
}

Node* BSTtoDLL(Node *root)
{
    Node *head=new Node(-1);
    Node *temp=head;
    Node *t;
    Node *curr=root;
    // Morris Inorder Traversal
    while (curr!=nullptr)
    {
        if(curr->left==nullptr)
        {
            temp->right=curr;
            curr->left=temp;
            temp=curr;
            curr=curr->right;
        }
        else
        {
            t=curr->left;
            while (t->right!=nullptr and t->right!=curr)
            {
                t=t->right;
            }
            if(t->right==nullptr)
            {
                t->right=curr;
                curr=curr->left;
            }
            else
            {
                t->right=nullptr;
                temp->right=curr;
                curr->left=temp;
                temp=curr;
                curr=curr->right;
            }
        }
    }
    head=head->right;
    head->left=nullptr;
    return head;
}

Node* MergeDLL(Node *head1,Node *head2)
{
    Node *head=new Node(-1);
    Node *temp=head;
    while (head1!=nullptr and head2!=nullptr)
    {
        if (head1->val<head2->val)
        {
            temp->right=head1;
            head1->left=temp;
            temp=head1;
            head1=head1->right;
        }
        else
        {
            temp->right=head2;
            head2->left=temp;
            temp=head2;
            head2=head2->right;
        }
    }
    if (head1!=nullptr)
    {
        temp->right=head1;
        head1->left=temp;
    }
    if(head2!=nullptr)
    {
        temp->right=head2;
        head2->left=temp;
    }
    head=head->right;
    head->left=nullptr;
    return head;
}

int LengthofDLL(Node *head)
{
    Node *temp=head;
    int count=0;
    while (temp!=nullptr)
    {
        count++;
        temp=temp->right;
    }
    return count;
}

Node *DLLtoBST(int n,Node *&head)
{
    if(n<=0 or head==nullptr)
    {
        return nullptr;
    }
    Node *left=DLLtoBST(n/2,head);
    Node *root=new Node(head->val);
    head=head->right;
    root->left=left;
    root->right=DLLtoBST(n-n/2-1,head);
    return root;
}

Node* MergeTwoBSTs(Node *root1,Node *root2)
{
    // 1. Convert BST ---> DLL
    Node *head1,*head2;
    head1=BSTtoDLL(root1);
    head2=BSTtoDLL(root2);
    
    // 2. Merge Two DLL
    Node *head;
    head=MergeDLL(head1,head2);
    // PrintDLL(head);

    // 3. DLL ----> BST
    int n=LengthofDLL(head);
    Node *root=DLLtoBST(n,head);
    return root;
}

int main()
{
    string str1,str2;
    getline(cin,str1);
    getline(cin,str2);
    vector<string> nodes1=Split(str1);
    vector<string> nodes2=Split(str2);
    Node *root1,*root2;
    root1=BuildTree(nodes1);
    root2=BuildTree(nodes2);
    Node *root;
    root=MergeTwoBSTs(root1,root2);
    Inorder(root);
    cout<<"\n";
    return 0;
}
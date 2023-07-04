// Binary Tree to Doubly Linked List

#include<iostream>
#include<vector>
#include<queue>
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

Node* BuildTree(vector<string> &nodes)
{
    int n=nodes.size();
    queue<Node*> q;
    if(n==0 or nodes[0]=="N")
    {
        return nullptr;
    }
    Node *root=new Node(stoi(nodes[0]));
    q.push(root);
    int i=1;
    Node *curr;
    while (!q.empty() and i<n)
    {
        curr=q.front();
        q.pop();
        
        // Left Child
        if(nodes[i]!="N")
        {
            curr->left=new Node(stoi(nodes[i]));
            q.push(curr->left);
        }
        i+=1;
        if (i>=n)
        {
            break;
        }
        // Right Child
        if(nodes[i]!="N")
        {
            curr->right=new Node(stoi(nodes[i]));
            q.push(curr->right);
        }
        i+=1;
    }
    return root;
}

void Inorder(Node *root)
{
    if (root==nullptr)
    {
        return;
    }
    Inorder(root->left);
    cout<<root->val<<" ";
    Inorder(root->right);
}

void BTtoDLL(Node *&temp,Node *root)
{
    if (root==nullptr)
    {
        return;
    }
    BTtoDLL(temp,root->left);
    temp->right=root;
    root->left=temp;
    temp=temp->right;
    BTtoDLL(temp,root->right);
}


void printhead(Node *head)
{
    Node *curr=head;
    while(curr!=nullptr)
    {
        cout<<curr->val<<" ";
        curr=curr->right;
    }
    cout<<"\n";
}

void printtail(Node *tail)
{
    Node *curr=tail;
    while(curr!=nullptr)
    {
        cout<<curr->val<<" ";
        curr=curr->left;
    }
    cout<<"\n";
}

int main()
{
    string str;
    getline(cin,str);
    vector<string> nodes;
    int i=0; 
    string temp="";
    while(i<str.size())
    {
        if(str[i]==' ')
        {
            nodes.push_back(temp);
            temp="";
        }
        else{
            temp+=str[i];
        }
        i+=1;
    }
    nodes.push_back(temp);
    Node *root;
    root=BuildTree(nodes);
    cout<<"Inorder Traversal: ";
    Inorder(root);
    cout<<"\n";
    Node *head,*tmp;
    head=new Node(-1);
    tmp=head;
    BTtoDLL(tmp,root);
    head=head->right;
    head->left=nullptr;
    Node *first,*last;
    first=head;
    last=first;
    while (last->right!=nullptr)
    {
        last=last->right;
    }
    cout<<"Print Head: ";
    printhead(first);
    cout<<"Print Tail: ";
    printtail(last);
    return 0;
}
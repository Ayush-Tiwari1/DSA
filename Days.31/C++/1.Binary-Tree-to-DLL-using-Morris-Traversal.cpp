// Binary Tree to Doubly Linked List using Morris Traversal

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

void Split(string &str,vector<string> &nodes)
{
    int i=0;
    int n=str.size();
    string temp="";
    while (i<n)
    {
        if (str[i]==' ')
        {
            nodes.push_back(temp);
            temp="";
        }
        else
        {
            temp+=str[i];
        }
        i+=1;
    }
    nodes.push_back(temp);
}

Node* BuildTree(vector<string> &nodes)
{
    queue<Node*> q;
    int n=nodes.size();
    if (n==0 or nodes[0]=="N")
    {
        return nullptr;
    }
    Node *root=new Node(stoi(nodes[0]));
    q.push(root);
    int i=1;
    Node *curr;
    while (i<n and !q.empty())
    {
        curr=q.front();
        q.pop();
        // Left Child
        if (nodes[i]!="N")
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
        if (nodes[i]!="N")
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
    if(root==nullptr)
    {
        return;
    }
    Inorder(root->left);
    cout<<root->val<<" ";
    Inorder(root->right);
}

vector<Node*> BTtoDLL(Node *root)
{
    vector<Node*> ans;
    Node *head,*tail;
    head=tail=new Node(-1);
    Node *temp,*curr,*t;
    temp=head;
    curr=root;
    while(curr!=nullptr)
    {
        if(curr->left==nullptr)
        {
            temp->right=curr;
            curr->left=temp;
            temp=curr;
            tail=temp;
            curr=curr->right;
        }
        else
        {
            t=curr->left;
            while(t->right!=nullptr and t->right!=curr)
            {
                t=t->right;
            }
            if (t->right==nullptr)
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
                tail=temp;
                curr=curr->right;
            }
        }
    }
    head=head->right;
    head->left=nullptr;
    ans.push_back(head);
    ans.push_back(tail);
    return ans;
}

void PrintHead(Node *head)
{
    Node *curr=head;
    while (curr!=nullptr)
    {
        cout<<curr->val<<" ";
        curr=curr->right;
    }
    cout<<"\n";
}

void PrintTail(Node *tail)
{
    Node *curr=tail;
    while (curr!=nullptr)
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
    Split(str,nodes);
    Node *root=BuildTree(nodes);
    cout<<"Inorder Traversal: ";
    Inorder(root);
    cout<<"\n";
    vector<Node*> ans=BTtoDLL(root);
    Node *head,*tail;
    head=ans[0];
    tail=ans[1];
    PrintHead(head);
    PrintTail(tail);
    return 0;
}
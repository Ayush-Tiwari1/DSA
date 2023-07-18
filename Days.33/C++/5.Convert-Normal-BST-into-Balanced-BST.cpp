// Convert a Normal BST ----> Balanced BST

#include<iostream>
#include<vector>
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


void Inputs(string &str,vector<string> &nodes)
{
    int i=0;
    string temp="";
    while(i<str.size())
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
        i++;
    }
    nodes.push_back(temp);
}

Node* BuildTree(vector<string> &nodes)
{
    int n=nodes.size();
    if (n==0 or nodes[0]=="N")
    {
        return nullptr;
    }
    Node *root=new Node(stoi(nodes[0]));
    int i=1;
    queue<Node*> q;
    q.push(root);
    Node *curr;
    while (!q.empty() and i<n)
    {
        curr=q.front();
        q.pop();
        if(nodes[i]!="N")
        {
            curr->left=new Node(stoi(nodes[i]));
            q.push(curr->left);
        }
        i++;
        if(i>=n)
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

void Inorder(Node* root,vector<int> &inorder)
{
    if(root==nullptr)
    {
        return;
    }
    Inorder(root->left,inorder);
    inorder.push_back(root->val);
    Inorder(root->right,inorder);
}

int isBalanced(Node *root,bool &flag)
{
    if(root==nullptr)
    {
        return 0;
    }
    int left=isBalanced(root->left,flag);
    int right=isBalanced(root->right,flag);
    if (abs(left-right)>1)
    {
        flag=false;
    }
    return max(left,right)+1;
}

Node* BalancedBST(int start,int end,vector<int> &inorder)
{
    if(start>end)
    {
        return nullptr;
    }
    if(start==end)
    {
        return new Node(inorder[start]);
    }
    int mid=(start+(end-start)/2);
    Node *root=new Node(inorder[mid]);
    root->left=BalancedBST(start,mid-1,inorder);
    root->right=BalancedBST(mid+1,end,inorder);
    return root;
}

int main()
{
    string str;
    getline(cin,str);
    vector<string> nodes;
    Inputs(str,nodes);
    Node *root=BuildTree(nodes);
    cout<<"Normal BST Balanced or Not:\t";
    bool flag=true;
    isBalanced(root,flag);
    if(flag)
    {
        cout<<"Yes\n";
    }
    else{
        cout<<"No\n";
    }
    vector<int> inorder;
    Inorder(root,inorder);
    Node *newroot=BalancedBST(0,inorder.size()-1,inorder);
    cout<<"Balanced BST Balanced or Not\t";
    flag=true;
    isBalanced(newroot,flag);
    if(flag)
    {
        cout<<"Yes\n";
    }
    else{
        cout<<"No\n";
    }
    return 0;
}
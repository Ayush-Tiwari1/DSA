// Construct BST from Level Order Traversal 

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

class Pair
{
    public:
    Node *root;
    int mini;
    int maxi;
};

Node* BuildBST(int n,vector<int> &level)
{
    Node *curr;
    int maxi;
    int mini;
    Node *root=new Node(level[0]);
    Pair p,temp;
    p.root=root;
    p.mini=INT_MIN;
    p.maxi=INT_MAX;
    queue<Pair> q;
    q.push(p);
    int i=1;
    while (i<n and !q.empty())
    {
        p=q.front();
        q.pop();
        curr=p.root;
        maxi=p.maxi;
        mini=p.mini;
        if (i<n and level[i]>mini and level[i]<maxi and level[i]<curr->val)
        {
            curr->left=new Node(level[i]);
            temp.root=curr->left;
            temp.mini=mini;
            temp.maxi=curr->val;
            i++;
            q.push(temp);
        }
        if(i<n and level[i]>mini and level[i]<maxi and level[i]>curr->val)
        {
            curr->right=new Node(level[i]);
            temp.root=curr->right;
            temp.mini=curr->val;
            temp.maxi=maxi;
            i++;
            q.push(temp);
        }
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
    cout<<root->val<< " ";
    Inorder(root->right);
}

int main()
{
    int n;
    cin>>n;
    vector<int> level(n);
    for(int i=0; i<n; i++)
    {
        cin>>level[i];
    }
    Node *root=BuildBST(n,level);
    Inorder(root);
    cout<<"\n";
    return 0;
}
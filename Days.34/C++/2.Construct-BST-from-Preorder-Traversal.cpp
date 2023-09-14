// Construct BST from Preorder Traversal

#include<iostream>
#include<climits>
#include<vector>
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

Node* BuildBST(int &indx,int n,vector<int> &preorder,int mini,int maxi)
{
    if(indx>=n)
    {
        return nullptr;
    }
    if(preorder[indx]<mini or preorder[indx]>maxi)
    {
        return nullptr;
    }
    Node *root=new Node(preorder[indx]);
    indx++;
    root->left=BuildBST(indx,n,preorder,mini,root->val);
    root->right=BuildBST(indx,n,preorder,root->val,maxi);
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
    vector<int> preorder(n);
    for(int i=0; i<n; i++)
    {
        cin>>preorder[i];
    }
    int indx=0;
    Node *root=BuildBST(indx,n,preorder,INT_MIN,INT_MAX);
    Inorder(root);
    cout<<"\n";
    return 0;
}
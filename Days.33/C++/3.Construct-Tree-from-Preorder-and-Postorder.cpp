// Construct Tree from Preorder and Postorder

#include<iostream>
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

Node *BuildTree(int pri,int pre,int poi,int poe,vector<int> &preorder,vector<int> &postorder)
{
    if (pri>pre or poi>poe)
    {
        return nullptr;
    }
    if( pri==pre and poi==poe)
    {
        return new Node(preorder[pri]);
    }
    Node *root=new Node(preorder[pri]);
    int indx,colse;
    indx=poi;
    while (postorder[indx]!=preorder[pri+1])
    {
        indx++;
    }
    colse=indx-poi+1;
    root->left=BuildTree(pri+1,pri+colse,poi,indx,preorder,postorder);
    root->right=BuildTree(pri+colse+1,pre,indx+1,poe-1,preorder,postorder);
    return root;
}

void Preorder(Node *root)
{
    if(root==nullptr)
    {
        return;
    }
    cout<<root->val<< " ";
    Preorder(root->left);
    Preorder(root->right);
}

void Postorder(Node *root)
{
    if (root==nullptr)
    {
        return;
    }
    Postorder(root->left);
    Postorder(root->right);
    cout<<root->val<<" ";
}

int main()
{
    int n;
    cin>>n;
    vector<int> preorder(n),postorder(n);
    for(int i=0; i<n; i++)
    {
        cin>>preorder[i];
    }    
    for(int i=0; i<n; i++)
    {
        cin>>postorder[i];
    }
    // BuildTree(pri,pre,poi,poe,preorder,postorder)
    // pri,pei ----> preorder starting index and ending index respectively
    // poi,poe ----> postorder starting index and ending index respectively
    Node *root=BuildTree(0,n-1,0,n-1,preorder,postorder);
    cout<<"Printing Preorder and Postorder:\n";
    Preorder(root);
    cout<<"\n";
    Postorder(root);
    cout<<"\n";
    return 0;
}
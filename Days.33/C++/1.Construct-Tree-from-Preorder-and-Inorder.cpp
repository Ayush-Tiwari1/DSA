// Construct Tree from Preorder and Inorder

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

Node* BuildTree(int psi,int pei,int isi,int iei,vector<int> &preorder,vector<int> &inorder)
{
    if (psi>pei or isi>iei)
    {
        return nullptr;
    }
    if(psi==pei and isi==iei)
    {
        return new Node(preorder[psi]);
    }
    Node *root=new Node(preorder[psi]);
    int indx=isi;
    while (inorder[indx]!=preorder[psi])
    {
        indx++;
    }
    // Count of Left Subtree Elements
    int colse=indx-isi;
    root->left=BuildTree(psi+1,psi+colse,isi,indx-1,preorder,inorder);
    root->right=BuildTree(psi+colse+1,pei,indx+1,iei,preorder,inorder);
    return root;
}

void Preorder(Node *root)
{
    if (root==nullptr)
    {
        return;
    }
    cout<<root->val<<" ";
    Preorder(root->left);
    Preorder(root->right);
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

int main()
{
    int n;
    cin>>n;
    vector<int> preorder(n),inorder(n);
    for(int i=0; i<n; i++)
    {
        cin>>preorder[i];
    }
    for(int i=0; i<n; i++)
    {
        cin>>inorder[i];
    }
    // BuildTree(psi,pei,isi,iei,preorder,inorder)
    // psi,pei----> preorder starting index and ending index respectively
    // isi,iei----> inorder starting index and ending index respectively
    Node *root=BuildTree(0,n-1,0,n-1,preorder,inorder);
    cout<<"Printing Preorder and Inorder:\n";
    Preorder(root);
    cout<<"\n";
    Inorder(root);
    return 0;
}
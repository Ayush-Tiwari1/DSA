// Construct Tree from Postorder and Inorder 

#include<iostream>
#include<vector>
using namespace std;

// 12
// 7 8 3 9 10 4 1 11 5 6 2 0
// 7 3 8 1 9 4 10 0 11 5 2 6
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

Node *BuildTree(int psi,int pei,int isi,int iei,vector<int> &postorder,vector<int> &inorder)
{
    if (psi>pei or isi>iei)
    {
        return nullptr;
    }
    if(psi==pei and isi==iei)
    {
        return new Node(postorder[psi]);
    }
    Node *root=new Node(postorder[pei]);
    int indx,colse;
    indx=isi;
    while (inorder[indx]!=postorder[pei])
    {
        indx++;
    }
    colse=indx-isi;
    root->left=BuildTree(psi,psi+colse-1,isi,indx-1,postorder,inorder);
    root->right=BuildTree(psi+colse,pei-1,indx+1,iei,postorder,inorder);
    return root;
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
    vector<int> postorder(n),inorder(n);
    for(int i=0; i<n; i++)
    {
        cin>>postorder[i];
    }
    for(int i=0; i<n; i++)
    {
        cin>>inorder[i];
    }
    Node *root=BuildTree(0,n-1,0,n-1,postorder,inorder);
    cout<<"Printing Postorder and Inorder:\n";
    Postorder(root);
    cout<<"\n";
    Inorder(root);
    return 0;
}
// Binary Search Tree

#include<iostream>
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

class BST
{
    public:
    Node *root;
    BST()
    {
        root=nullptr;
    }
    Node *Insert(Node *root,int val)
    {
        if (root==nullptr)
        {
            return new Node(val);
        }
        if (root->val==val)
        {
            return root;
        }
        if (root->val>val)
        {
            root->left=Insert(root->left,val);
        }
        else
        {
            root->right=Insert(root->right,val);
        }
        return root;
    }

    bool Search(Node *root,int val)
    {
        if(root==nullptr)
        {
            return false;
        }
        if(root->val==val)
        {
            return true;
        }
        if (root->val>val)
        {
            return Search(root->left,val);
        }
        else{
            return Search(root->right,val);
        }
    }

    Node* Delete(Node *root,int val)
    {
        if (root==nullptr)
        {
            return nullptr;
        }
        if(root->val==val)
        {
            if(root->left!=nullptr and root->right!=nullptr)
            {
                Node *temp=root->left;
                while (temp->right!=nullptr)
                {
                    temp=temp->right;
                }
                root->val=temp->val;
                root->left=Delete(root->left,temp->val);
                return root;
            }
            if(root->left!=nullptr)
            {
                return root->left;
            }
            else{
                return root->right;
            }
        }
        if(root->val>val)
        {
            root->left=Delete(root->left,val);
        }
        else{
            root->right=Delete(root->right,val);
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
};

int main()
{
    BST *bst=new BST();
    int val,choice;
    while (true)
    {
        cout<<"1.Insert\n";
        cout<<"2.Delete\n";
        cout<<"3.Search\n";
        cout<<"4.Inorder Traversal\n";
        cout<<"5.Exit\n";
        cout<<"Enter Your Choice:\t";
        cin>>choice;
        if (choice==1)
        {
            cout<<"Enter a Value:\t";
            cin>>val;
            bst->root=bst->Insert(bst->root,val);
        }
        else if(choice==2)
        {
            cout<<"Enter Value to be Deleted:\t";
            cin>>val;
            if(bst->Search(bst->root,val))
            {
                bst->root=bst->Delete(bst->root,val);
                cout<<"Deleted Successfully\n";
            }
            else{
                cout<<"Not Present in BST\n";
            }
        }
        else if(choice==3)
        {
            cout<<"Enter value for Searching:\t";
            cin>>val;
            if (bst->Search(bst->root,val))
            {
                cout<<"Present in BST\n";
            }
            else
            {
                cout<<"Not Present in BST\n";
            }
        }
        else if(choice==4)
        {
            bst->Inorder(bst->root);
            cout<<"\n";
        }
        else if(choice==5)
        {
            break;
        }
        else{
            cout<<"Invalid Choice\n";
        }
    }
    return 0;
}
# Construct BST from Preorder Traversal

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def BuildBST(indx,n,preorder,mini,maxi):
    if indx[0]>=n:
        return None
    if preorder[indx[0]]<mini or preorder[indx[0]]>maxi:
        return None
    root=Node(preorder[indx[0]])
    indx[0]+=1
    root.left=BuildBST(indx,n,preorder,mini,root.val)
    root.right=BuildBST(indx,n,preorder,root.val,maxi)
    return root

def Inorder(root):
    if root==None:
        return
    Inorder(root.left)
    print(root.val,end=" ")
    Inorder(root.right)

def main():
    n=int(input())
    preorder=list(map(int,input().split()))
    indx=[0]
    root=BuildBST(indx,n,preorder,-2**63,2**63)
    Inorder(root)
    print()




main()


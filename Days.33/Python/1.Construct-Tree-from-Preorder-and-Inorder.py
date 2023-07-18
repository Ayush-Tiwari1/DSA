# Construct Tree from Preorder and Inorder

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def Preorder(root):
    if root==None:
        return
    print(root.val,end=" ")
    Preorder(root.left)
    Preorder(root.right)

def Inorder(root):
    if root==None:
        return
    Inorder(root.left)
    print(root.val,end=" ")
    Inorder(root.right)

def BuildTree(psi,pei,isi,iei,preorder,inorder):
    if psi>pei or isi>iei:
        return None
    if psi==pei and isi==iei:
        return Node(preorder[psi])
    root=Node(preorder[psi])
    indx=isi
    while inorder[indx]!=preorder[psi]:
        indx+=1
    # Count of Left Subtree Elements
    colse=indx-isi
    root.left=BuildTree(psi+1,psi+colse,isi,indx-1,preorder,inorder)
    root.right=BuildTree(psi+colse+1,pei,indx+1,iei,preorder,inorder)
    return root

def main():
    n=int(input())
    preorder=list(map(int,input().split()))
    inorder=list(map(int,input().split()))
    # BuildTree(psi,pei,isi,iei,preorder,inorder)
    # psi,pei---> Preorder starting index and ending index respectively
    # isi,iei---> Inorder starting index and endding index respectively
    root=BuildTree(0,n-1,0,n-1,preorder,inorder)
    print('Printing Preorder and Inorder:')
    Preorder(root)
    print()
    Inorder(root)

main()
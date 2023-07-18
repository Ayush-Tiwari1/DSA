# Construct Tree from Postorder and Inorder

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def BuildTree(psi,pei,isi,iei,postorder,inorder):
    if psi>pei or isi>iei:
        return None
    if psi==pei and isi==iei:
        return Node(postorder[psi])
    root=Node(postorder[pei])
    indx=isi
    while inorder[indx]!=postorder[pei]:
        indx+=1
    colse=indx-isi
    root.left=BuildTree(psi,psi+colse-1,isi,indx-1,postorder,inorder)
    root.right=BuildTree(psi+colse,pei-1,indx+1,iei,postorder,inorder)
    return root

def Postorder(root):
    if root==None:
        return
    Postorder(root.left)
    Postorder(root.right)
    print(root.val,end=" ")

def Inorder(root):
    if root==None:
        return
    Inorder(root.left)
    print(root.val,end=" ")
    Inorder(root.right)

def main():
    n=int(input())
    postorder=list(map(int,input().split()))
    inorder=list(map(int,input().split()))
    # BuildTree(psi,pei,isi,iei,postorder,inorder)
    # psi,pei ---> Postorder starting index and ending index respectively
    # isi,iei ---> Inorder starting index and ending index respectively
    root=BuildTree(0,n-1,0,n-1,postorder,inorder)
    print('Printing Postorder and Inorder:')
    Postorder(root)
    print()
    Inorder(root)
main()
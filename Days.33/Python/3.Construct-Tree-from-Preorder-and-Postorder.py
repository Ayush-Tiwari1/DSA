# Construct Tree from Preorder and Postorder

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def BuildTree(pri,pre,poi,poe,preorder,postorder):
    if pri>pre and poi>poe:
        return None
    if pri==pre and poi==poe:
        return Node(preorder[pri])
    root=Node(preorder[pri])
    indx=poi
    while postorder[indx]!=preorder[pri+1]:
        indx+=1
    colse=(indx-poi+1)
    root.left=BuildTree(pri+1,pri+colse,poi,indx,preorder,postorder)
    root.right=BuildTree(pri+colse+1,pre,indx+1,poe-1,preorder,postorder)
    return root

def Preorder(root):
    if root==None:
        return
    print(root.val,end= " ")
    Preorder(root.left)
    Preorder(root.right)

def Postorder(root):
    if root==None:
        return 
    Postorder(root.left)
    Postorder(root.right)
    print(root.val,end=" ")

def main():
    n=int(input())
    preorder=list(map(int,input().split()))
    postorder=list(map(int,input().split()))
    # BuildTree(pri,pre,poi,poe,preorder,postorder)
    # pri,pre ---> preorder starting index and ending index respectively
    # poi,poe ---> postorder staring index and ending index respectively
    root=BuildTree(0,n-1,0,n-1,preorder,postorder)
    print('Printing Postorder and Preorder:')
    Preorder(root)
    print()
    Postorder(root)
    print()

main()
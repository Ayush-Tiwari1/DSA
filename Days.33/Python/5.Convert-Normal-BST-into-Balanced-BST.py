# Convert a Normal BST ----> Balanced BST

from collections import deque

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def BuildTree(str):
    if len(str)==0 or str[0]=='N':
        return None
    dq=deque()
    root=Node(int(str[0]))
    dq.append(root)
    i=1
    n=len(str)
    while dq and i<n:
        curr=dq.popleft()
        if str[i]!='N':
            curr.left=Node(int(str[i]))
            dq.append(curr.left)
        i+=1
        if i>=n:
            break
        if str[i]!='N':
            curr.right=Node(int(str[i]))
            dq.append(curr.right)
        i+=1
    return root

def Inorder(root,inorder):
    if root==None:
        return
    Inorder(root.left,inorder)
    inorder.append(root.val)
    Inorder(root.right,inorder)

def BST(start,end,inorder):
    if start>end:
        return None
    if start==end:
        return Node(inorder[start])
    mid=(start+end)//2
    root=Node(inorder[mid])
    root.left=BST(start,mid-1,inorder)
    root.right=BST(mid+1,end,inorder)
    return root

def BalancedBST(root):
    inorder=[]
    Inorder(root,inorder)
    return BST(0,len(inorder)-1,inorder)

def Balanced(root,flag):
    if root==None:
        return 0
    left=Balanced(root.left,flag)
    right=Balanced(root.right,flag)
    h=abs(left-right)
    if h>1:
        flag[0]=False
    return max(left,right)+1
def main():
    str=input().split()
    root=BuildTree(str)
    flag=[True]
    newroot=BalancedBST(root)
    Balanced(newroot,flag)
    if flag[0]==True:
        print('Tree is Balanced Now')
    else:
        print('Tree is Not Balanced')
main()


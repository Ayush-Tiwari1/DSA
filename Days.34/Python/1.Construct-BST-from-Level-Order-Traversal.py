# Construct BST from its Level Order Traversal

from collections import deque

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def BuildBST(n,level):
    dq=deque()
    root=Node(level[0])
    dq.append([root,-2**63,2**63])
    i=1
    while i<n and dq:
        curr,mini,maxi=dq.popleft()
        if i<n and level[i]>mini and level[i]<maxi and level[i]<curr.val:
            curr.left=Node(level[i])
            dq.append([curr.left,mini,curr.val])
            i+=1
        if i<n and level[i]>mini and level[i]<maxi and level[i]>curr.val:
            curr.right=Node(level[i])
            dq.append([curr.right,curr.val,maxi])
            i+=1
    return root

def Inorder(root):
    if root==None:
        return
    Inorder(root.left)
    print(root.val,end= " ")
    Inorder(root.right)

def main():
    n=int(input())
    level=list(map(int,input().split()))
    root=BuildBST(n,level)
    Inorder(root)
    print()



main()


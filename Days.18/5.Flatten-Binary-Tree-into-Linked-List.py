from collections import deque

class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

def BuildTree(s):
    nodes=s.split()
    n=len(nodes)
    if n==0 or nodes[0]=='N':
        return None
    root=Node(int(nodes[0]))
    dq=deque()
    dq.append(root)
    size=1
    i=1
    while size>0 and i<n:
        temp=dq.popleft()
        size-=1
        if nodes[i]!='N':
            temp.left=Node(int(nodes[i]))
            dq.append(temp.left)
            size+=1
        i+=1
        if i>=n:
            break
        if nodes[i]!='N':
            temp.right=Node(int(nodes[i]))
            dq.append(temp.right)
            size+=1
        i+=1
    return root

def FlattenBinaryTree(root):
    head=root
    curr=root
    while curr!=None:
        if curr.left==None:
            curr=curr.right
        else:
            temp=curr.left
            while temp.right!=None:
                temp=temp.right
            temp.right=curr.right
            curr.right=curr.left
            curr.left=None
            curr=curr.right
    return head


def Inorder(root):
    if root==None:
        return
    Inorder(root.left)
    print(root.data,end=" ")
    Inorder(root.right)

def main():
    s=input()
    root=BuildTree(s)
    Inorder(root)
    print()
    head=FlattenBinaryTree(root)
    Inorder(head)
    print()
if __name__=='__main__':
    main()
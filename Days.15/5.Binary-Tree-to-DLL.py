from collections import deque
class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

class Tree:
    def __init__(self):
        self.head=None
        self.temp=None
    def BuildTree(self,s):
        nodes=s.split()
        n=len(nodes)
        if n==0 or nodes[0]=='N':
            return None
        dq=deque()
        root=Node(int(nodes[0]))
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
    def Inorder(self,root):
        if root==None:
            return
        self.Inorder(root.left)
        print(root.data,end=" ")
        self.Inorder(root.right)
    def BinaryTreetoDLL(self,root):
        if root==None:
            return
        self.BinaryTreetoDLL(root.left)
        self.temp.right=root
        root.left=self.temp
        self.temp=self.temp.right
        self.BinaryTreetoDLL(root.right)
def main():
    s=input()
    tree=Tree()
    root=tree.BuildTree(s)
    tree.Inorder(root)
    tree.head=Node(-1)
    tree.temp=tree.head
    tree.BinaryTreetoDLL(root)
    tree.head=tree.head.right
    tree.head.left=None
    tree.temp=tree.head
    temp=tree.head
    print()
    print('left to right traversal:',end=" ")
    prev=None
    while temp!=None:
        prev=temp
        print(temp.data,end=" ")
        temp=temp.right
    print()
    print('right to left traversal',end=" ")
    while prev!=None:
        print(prev.data,end=" ")
        prev=prev.left

if __name__=='__main__':
    main()
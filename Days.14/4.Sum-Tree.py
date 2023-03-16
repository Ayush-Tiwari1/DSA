from collections import deque
class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

class Tree:
    def __init__(self):
        self.flag=True
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
    def SumTree(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return root.data 
        left=self.SumTree(root.left)
        right=self.SumTree(root.right)
        if left+right!=root.data:
            self.flag=False
        return 2*root.data 
def main():
    s=input()
    tree=Tree()
    root=tree.BuildTree(s)
    tree.Inorder(root)
    print()
    tree.flag=True
    tree.SumTree(root)
    if tree.flag==True:
        print('Sum Tree')
    else:
        print('Not Sum Tree')
if __name__=='__main__':
    main()
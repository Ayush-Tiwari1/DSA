from collections import deque
class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

class Tree:
    def BuildTree(self,s):
        q=deque()
        list=s.split()
        root=Node(int(list[0]))
        q.append(root)
        i=1
        size=1
        while size>0 and i<len(list):
            temp=q.popleft()
            size-=1
            if list[i]!='N':
                temp.left=Node(int(list[i]))
                q.append(temp.left)
                size+=1
            i+=1
            if i>=len(list):
                break
            if list[i]!='N':
                temp.right=Node(int(list[i]))
                q.append(temp.right)
                size+=1
            i+=1
        return root
    def Inorder(self,root):
        if root==None:
            return
        self.Inorder(root.left)
        print(root.data,end=" ")
        self.Inorder(root.right)
    def PreOrder(self,root):
        if root==None:
            return
        print(root.data,end=" ")
        self.PreOrder(root.left)
        self.PreOrder(root.right)
    def PostOrder(self,root):
        if root==None:
            return
        self.PostOrder(root.left)
        self.PostOrder(root.right)
        print(root.data,end=" ")
    def LevelOrderTraversal(self,root):
        q=deque()
        q.append(root)
        size=1
        while size>0:
            temp=q.popleft()
            size-=1
            print(temp.data,end=" ")
            if temp.left!=None:
                q.append(temp.left)
                size+=1
            if temp.right!=None:
                q.append(temp.right)
                size+=1
    def Height(self,root):
        if root==None:
            return 0
        return max(self.Height(root.left),self.Height(root.right))+1
def main():
    s=input()
    tree=Tree()
    root=tree.BuildTree(s)
    print('Inorder Traversal:',end=" ")
    tree.Inorder(root)
    print()
    print('LevelOrder Traversal:',end=" ")
    tree.LevelOrderTraversal(root)
    print()
    print('PreOrder Traversal:',end=" ")
    tree.PreOrder(root)
    print()
    print('PostOrder Traversal:',end=" ")
    tree.PostOrder(root)
    print()
    print('Height:',end=" ")
    print(tree.Height(root))

if __name__=='__main__':
    main()

class Node:
    def __init__(self,val):
        self.left=None 
        self.data=val
        self.right=None

class Tree:
    def Insert(self,root,data):
        if root==None:
            return Node(data)
        if root.data<data:
            root.right=self.Insert(root.right,data)
        elif root.data>data:
            root.left=self.Insert(root.left,data)
        return root
    def Inorder(self,root):
        if root==None:
            return
        self.Inorder(root.left)
        print(root.data,end=" ")
        self.Inorder(root.right)

def main():
    n=int(input())
    nodes=list(map(int,input().split()))
    root=None
    tree=Tree()
    for i in range(n):
        root=tree.Insert(root,nodes[i])
    tree.Inorder(root)
if __name__=='__main__':
    main()
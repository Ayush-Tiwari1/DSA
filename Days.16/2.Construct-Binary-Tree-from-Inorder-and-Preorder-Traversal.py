
class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

class Tree:
    def __init__(self):
        self.i=0
    def Search(self,inorder,start,end,val):
        for i in range(start,end+1):
            if inorder[i]==val:
                return i
        return -1
    def ConstructTree(self,start,end,n,preorder,inorder):
        if start>end or self.i==n:
            return None
        root=Node(preorder[self.i])
        indx=self.Search(inorder,start,end,preorder[self.i])
        self.i+=1
        root.left=self.ConstructTree(start,indx-1,n,preorder,inorder)
        root.right=self.ConstructTree(indx+1,end,n,preorder,inorder)
        return root

    def Inorder(self,root):
        if root==None:
            return
        self.Inorder(root.left)
        print(root.data,end= " ")
        self.Inorder(root.right)

def main():
    n=int(input())
    inorder=list(map(int,input().split()))
    preorder=list(map(int,input().split()))
    tree=Tree()
    tree.i=0
    root=tree.ConstructTree(0,n-1,n,preorder,inorder)
    tree.Inorder(root)

if __name__=='__main__':
    main()
from collections import deque
class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

class Tree:
    def BuildTree(self,s):
        nodes=s.split()
        n=len(nodes)
        if n==0 or nodes[0]=='N':
            return None
        dq=deque()
        root=Node(int(nodes[0]))
        size=1
        i=1
        dq.append(root)
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
    def LeftNodes(self,root):
        l=[]
        if root==None:
            return l
        while root.left!=None or root.right!=None:
            l.append(root.data)
            if root.left!=None:
                root=root.left
            else:
                root=root.right
        return l
    def RightNodes(self,root):
        r=[]
        if root==None:
            return r
        while root.left!=None or root.right!=None:
            r.append(root.data)
            if root.right!=None:
                root=root.right
            else:
                root=root.left
        return r
    def LeafNodes(self,root,leaf):
        if root==None:
            return
        self.LeafNodes(root.left,leaf)
        if root.left==None and root.right==None:
            leaf.append(root.data)
        self.LeafNodes(root.right,leaf)
    def BoundaryTraversal(self,root):
        if root==None:
            return []
        if root.left==None and root.right==None:
            return [root.data]
        l=self.LeftNodes(root.left)
        r=self.RightNodes(root.right)
        leaf=[]
        self.LeafNodes(root,leaf)
        ans=[]
        ans.append(root.data)
        for val in l:
            ans.append(val)
        for val in leaf:
            ans.append(val)
        for i in range(len(r)-1,-1,-1):
            ans.append(r[i])
        return ans
def main():
    s=input()
    tree=Tree()
    root=tree.BuildTree(s)
    tree.Inorder(root)
    print()
    ans=tree.BoundaryTraversal(root)
    for val in ans:
        print(val,end=" ")


if __name__=='__main__':
    main()
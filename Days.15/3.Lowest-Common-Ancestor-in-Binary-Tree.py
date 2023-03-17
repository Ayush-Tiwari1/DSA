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
    def InOrder(self,root):
        if root==None:
            return
        self.InOrder(root.left)
        print(root.data,end=" ")
        self.InOrder(root.right)
    def LCA(self,root,n1,n2):
        if root==None:
            return None
        left=self.LCA(root.left,n1,n2)
        right=self.LCA(root.right,n1,n2)
        if left!=None and right!=None:
            return root
        if root.data==n1 or root.data==n2:
            return root
        if left!=None:
            return left
        return right

def main():
    s=input()
    n1,n2=map(int,input().split())
    tree=Tree()
    root=tree.BuildTree(s)
    tree.InOrder(root)
    ans=tree.LCA(root,n1,n2)
    print()
    if ans==None:
        print(-1)
    else:
        print(ans.data)
if __name__=='__main__':
    main()
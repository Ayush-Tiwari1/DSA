from collections import deque
class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

class Tree:
    def __init__(self):
        self.ans=-1
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
            #Build left node
            if nodes[i]!='N':
                temp.left=Node(int(nodes[i]))
                dq.append(temp.left)
                size+=1
            i+=1
            if i>=n:
                break
            #Build right node
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
    def MinDistance(self,root,a,b):
        if root==None:
            return 0
        left=self.MinDistance(root.left,a,b)
        right=self.MinDistance(root.right,a,b)
        if root.data==a or root.data==b:
            if left!=0:
                self.ans=left
            elif right!=0:
                self.ans=right
            return 1
        if left!=0 and right!=0:
            self.ans=left+right
            return 0
        elif left!=0:
            return left+1
        elif right!=0:
            return right+1
        else:
            return 0

def main():
    s=input()
    a,b=map(int,input().split())
    tree=Tree()
    root=tree.BuildTree(s)
    tree.Inorder(root)
    tree.ans=-1
    print()
    print('Minimum Distance between',a,'and',b,'is',tree.ans)

if __name__=='__main__':
    main()
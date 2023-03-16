from collections import deque
class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

class Tree:
    def __init__(self):
        self.maxsum=-2**63
    
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
    def Inorder(self,root):
        if root==None:
            return
        self.Inorder(root.left)
        print(root.data,end=" ")
        self.Inorder(root.right)
    def MaxPathSum(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return root.data
        left=self.MaxPathSum(root.left)
        right=self.MaxPathSum(root.right)
        if root.left!=None and root.right!=None:
            self.maxsum=max(self.maxsum,left+right+root.data)
            return (max(left,right)+root.data)
        if root.left!=None:
            return root.data+left
        else:
            return root.data+right
    def maxPathSum(self, root):
        INT_MIN=-2**63
        self.maxsum=INT_MIN
        val=self.MaxPathSum(root)
        if root.left==None or root.right==None:
            self.maxsum=max(self.maxsum,val)
        return self.maxsum
def main():
    s=input()
    tree=Tree()
    root=tree.BuildTree(s)
    tree.Inorder(root)
    print()
    tree.maxsum=0
    tree.maxPathSum(root)
    print('Maximum Path Sum between 2 Special Nodes is:',tree.maxsum)

if __name__=='__main__':
    main()
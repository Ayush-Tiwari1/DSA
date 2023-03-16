from collections import deque
class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

class BST:
    def BuildTree(self,s):
        nodes=s.split()
        if len(nodes)==0 or nodes[0]=='N':
            return None
        dq=deque()
        root=Node(int(nodes[0]))
        dq.append(root)
        size=1
        i=1
        n=len(nodes)
        while size>0 and i<n:
            temp=dq.popleft()
            size-=1
            if nodes[i]!='N':
                temp.left=Node(int(nodes[i]))
                size+=1
                dq.append(temp.left)
            i+=1
            if i>=n:
                break
            if nodes[i]!='N':
                temp.right=Node(int(nodes[i]))
                size+=1
                dq.append(temp.right)
            i+=1
        return root
    def Inorder(self,root):
        if root==None:
            return
        self.Inorder(root.left)
        print(root.data,end=" ")
        self.Inorder(root.right)
    def CheckBST(self,root,mini,maxi):
        if root==None:
            return True
        if root.data>=maxi or root.data<=mini:
            return False
        l=self.CheckBST(root.left,mini,root.data)
        r=self.CheckBST(root.right,root.data,maxi)
        if l==False or r==False:
            return False
        return True

def main():
    s=input()
    bst=BST()
    root=bst.BuildTree(s)
    bst.Inorder(root)
    b=bst.CheckBST(root,-2**63,2**63)
    print()
    if b== True:
        print('BST')
    else:
        print('Not BST')
if __name__=='__main__':
    main()
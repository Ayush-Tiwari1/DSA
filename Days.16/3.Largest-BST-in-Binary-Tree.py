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
    def Inorder(self,root):
        if root==None:
            return
        self.Inorder(root.left)
        print(root.data,end=" ")
        self.Inorder(root.right)
    def BST(self,root):
        if root==None:
            return [True,2**63,-2**63,0]
        if root.left==None and root.right==None:
            return [True,root.data,root.data,1]
        l=self.BST(root.left)
        r=self.BST(root.right)
        if l[0]==True and r[0]==True and root.data>l[2] and root.data<r[1]:
                val1=l[1]
                val2=r[2]
                val1=min(val1,root.data)
                val2=max(val2,root.data)
                return [True,val1,val2,l[3]+r[3]+1]
        return [False,2**63,-2**63,max(r[3],l[3])]



def main():
    s=input()
    tree=Tree()
    root=tree.BuildTree(s)
    print('Inorder:',end=" ")
    tree.Inorder(root)
    print()
    #[Bool,min,max,length]
    ans=tree.BST(root)
    print('BST size:',ans[3])

if __name__=='__main__':
    main()
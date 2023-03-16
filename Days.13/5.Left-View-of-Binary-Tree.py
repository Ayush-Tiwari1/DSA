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
        i=1
        size=1
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
    def LeftView(self,root):
        if root==None:
            return []
        dq=deque()
        dq.append(root)
        size=1
        ans=[]
        while size>0:
            currsize=len(dq)
            for _ in range(currsize):
                temp=dq.popleft()
                size-=1
                if _==0:
                    ans.append(temp.data)
                if temp.left!=None:
                    dq.append(temp.left)
                    size+=1
                if temp.right!=None:
                    dq.append(temp.right)
                    size+=1
        return ans
def main():
    s=input()
    tree=Tree()
    root=tree.BuildTree(s)
    tree.Inorder(root)
    #Left View of Binary Tree
    print()
    ans=tree.LeftView(root)
    for val in ans:
        print(val,end=" ")

if __name__ =='__main__':
    main()
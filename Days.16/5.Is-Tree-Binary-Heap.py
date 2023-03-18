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
        dq.append(root)
        size=1
        i=1
        while size>0 and i<n:
            temp=dq.popleft()
            size-=1
            #Left node
            if nodes[i]!='N':
                temp.left=Node(int(nodes[i]))
                dq.append(temp.left)
                size+=1
            i+=1
            if i>=n:
                break
            #Right node
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
    def isHeap(self,root):
        dq=deque()
        dq.append(root)
        while True:
            temp=dq.popleft()
            if temp==None:
                break
            left=temp.left
            right=temp.right
            dq.append(left)
            dq.append(right)
            if left!=None and root.data<left.data:
                return False
            if right!=None and root.data<right.data:
                return False
        while len(dq)>0:
            temp=dq.popleft()
            if temp!=None:
                return False
        
        return True


def main():
    s=input()
    tree=Tree()
    root=tree.BuildTree(s)
    tree.Inorder(root)
    ans=tree.isHeap(root)
    if ans==True:
        print('Binary Heap')
    else:
        print('Not Binary Heap')


if __name__=='__main__':
    main()
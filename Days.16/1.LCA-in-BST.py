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
        temp=root
        while temp!=None:
            if temp.data>n1 and temp.data>n2:
                temp=temp.left
            elif temp.data<n1 and temp.data<n2:
                temp=temp.right
            else:
                return temp.data
        return -1

def main():
    s=input()
    n1,n2=map(int,input().split())
    tree=Tree()
    root=tree.BuildTree(s)
    tree.InOrder(root)
    ans=tree.LCA(root,n1,n2)
    print()
    print(ans)

if __name__=='__main__':
    main()
from collections import deque
class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

class Tree:
    def __init__(self):
        self.diameter=1
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
        print(root.data,end= " ")
        self.Inorder(root.right)
    def Diameter(self,root):
        if root==None:
            return 0
        left=self.Diameter(root.left)
        right=self.Diameter(root.right)
        self.diameter=max(self.diameter,left+right+1)
        return max(left,right)+1

def main():
    s=input()
    tree=Tree()
    root=tree.BuildTree(s)
    tree.Inorder(root)
    tree.diameter=1
    ans=tree.Diameter(root)
    tree.diameter=max(ans,tree.diameter)
    print('Diameter:',tree.diameter)

if __name__=='__main__':
    main()
from collections import deque

class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

class Tree:
    def __init__(self):
        self.in1=''
        self.in2=''
        self.pre1=''
        self.pre2=''
    def BuildTree(self,s):
        nodes=s.split()
        n=len(nodes)
        if n==0 or nodes[0]=='N':
            return None
        root=Node(nodes[0])
        dq=deque()
        dq.append(root)
        size=1
        i=1
        while size>0 and i<n:
            temp=dq.popleft()
            size-=1
            if nodes[i]!='N':
                temp.left=Node(nodes[i])
                dq.append(temp.left)
                size+=1
            i+=1
            if i>=n:
                break
            if nodes[i]!='N':
                temp.right=Node(nodes[i])
                dq.append(temp.right)
                size+=1
            i+=1
        return root
    # def Inorder(self,root):
    #     if root==None:
    #         return
    #     self.Inorder(root.left)
    #     print(root.data,end=" ")
    #     self.Inorder(root.right)
    def Inorder1(self,root):
        if root==None:
            self.in1+='$'
            return
        self.Inorder1(root.left)
        self.in1+=str(root.data)
        self.Inorder1(root.right)
    def Preorder1(self,root):
        if root==None:
            self.pre1+='$'
            return
        self.pre1+=str(root.data)
        self.Preorder1(root.left)
        self.Preorder1(root.right)
    def Inorder2(self,root):
        if root==None:
            self.in2+='$'
            return
        self.Inorder2(root.left)
        self.in2+=str(root.data)
        self.Inorder2(root.right)
    def Preorder2(self,root):
        if root==None:
            self.pre2+='$'
            return
        self.pre2+=str(root.data)
        self.Preorder2(root.left)
        self.Preorder2(root.right)
    def isSubTree(self,root1,root2):
        if root2==None:
            return True
        if root1==None:
            return False
        self.in1=''
        self.in2=''
        self.pre1=''
        self.pre2=''
        self.Inorder1(root1)
        self.Inorder2(root2)
        flag=False
        if self.in2 in self.in1:
            flag=True
        else:
            flag=False
        if flag==False:
            return False
        self.Preorder1(root1)
        self.Preorder2(root2)
        # print(self.in1,self.in2)
        # print(self.pre1,self.pre2)
        if self.pre2 in self.pre1:
            flag=True
        else:
            flag=False
        return flag

def main():
    s1=input()
    s2=input()
    tree=Tree()
    root1=tree.BuildTree(s1)
    root2=tree.BuildTree(s2)
    ans=tree.isSubTree(root1,root2)
    if ans==True:
        print('Yes')
    else:
        print('No')

if __name__=='__main__':
    main()
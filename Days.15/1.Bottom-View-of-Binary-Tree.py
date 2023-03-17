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
    
    def BottomView(self,root):
        dict={}
        dq=deque()
        dq.append([root,0])
        size=1
        while size>0:
            temp=dq.popleft()
            size-=1
            dict[temp[1]]=temp[0].data 
            if temp[0].left!=None:
                dq.append([temp[0].left,temp[1]-1])
                size+=1
            if temp[0].right!=None:
                dq.append([temp[0].right,temp[1]+1])
                size+=1
        values=[]
        for i in dict:
            values.append([i,dict[i]])
        values.sort()
        ans=[]
        for val in values:
            ans.append(val[1])
        return ans

def main():
    s=input()
    tree=Tree()
    root=tree.BuildTree(s)
    print('Inorder Traversal:',end=" ")
    tree.InOrder(root)
    ans=tree.BottomView(root)
    print()
    print('Bottom View:',end=" ")
    for val in ans:
        print(val,end=" ")

if __name__=='__main__':
    main()
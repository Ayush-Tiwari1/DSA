from collections import deque

class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

def BuildTree(s):
    nodes=s.split()
    n=len(nodes)
    if n==0 or nodes[0]=='N':
        return None
    root=Node(int(nodes[0]))
    dq=deque()
    dq.append(root)
    indx=1
    while len(dq)>0 and indx<n:
        temp=dq.popleft()
        if nodes[indx]!='N':
            temp.left=Node(int(nodes[indx]))
            dq.append(temp.left)
        indx+=1
        if indx>=n:
            break
        if nodes[indx]!='N':
            temp.right=Node(int(nodes[indx]))
            dq.append(temp.right)
        indx+=1
    
    return root

def Preorder(root):
    if root==None:
        return
    print(root.data,end=" ")
    Preorder(root.left)
    Preorder(root.right)

def MorrisPreorder(root):
    curr=root
    while curr!=None:
        if curr.left==None:
            print(curr.data,end=" ")
            curr=curr.right
        else:
            temp=curr.left
            while temp.right!=None and temp.right!=curr:
                temp=temp.right
            if temp.right==None:
                print(curr.data,end=" ")
                temp.right=curr
                curr=curr.left
            else:
                temp.right=None
                curr=curr.right

def main():
    s=input()
    root=BuildTree(s)
    print('Recursive Preorder:',end=" ")
    Preorder(root)
    print()
    print('Morris Preorder:',end=" ")
    MorrisPreorder(root)
    print()

if __name__=='__main__':
    main()
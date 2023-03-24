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
    dq=deque()
    root=Node(int(nodes[0]))
    dq.append(root)
    i=1
    while len(dq)>0 and i<n:
        temp=dq.popleft()
        if nodes[i]!='N':
            temp.left=Node(int(nodes[i]))
            dq.append(temp.left)
        i+=1
        if i>=n:
            break
        if nodes[i]!='N':
            temp.right=Node(int(nodes[i]))
            dq.append(temp.right)
        i+=1
    return root

def Inorder(root):
    if root==None:
        return
    Inorder(root.left)
    print(root.data,end=" ")
    Inorder(root.right)

def main():
    s=input()
    root=BuildTree(s)
    print('Recursive Inorder:')
    Inorder(root)
    print()
    print('Morris Inorder Traversal:')
    MorrisInorder(root)
    print()
def MorrisInorder(root):
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
                temp.right=curr
                curr=curr.left
            else:
                print(curr.data,end=" ")
                temp.right=None
                curr=curr.right

if __name__=='__main__':
    main()


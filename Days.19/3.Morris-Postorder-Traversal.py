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
        if nodes[i]!='N':
            temp.right=Node(int(nodes[i]))
            dq.append(temp.right)
        i+=1
    return root

def Postorder(root):
    if root==None:
        return
    Postorder(root.left)
    Postorder(root.right)
    print(root.data,end=" ")

def MorrisPostorder(root):
    curr=root
    post=[]
    while curr!=None:
        if curr.right==None:
            post.append(curr.data)
            curr=curr.left
        else:
            temp=curr.right
            while temp.left!=None and temp.left!=curr:
                temp=temp.left
            if temp.left==None:
                post.append(curr.data)
                temp.left=curr
                curr=curr.right
            else:
                temp.left=None
                curr=curr.left
    post.reverse()
    for val in post:
        print(val,end=" ")

def main():
    s=input()
    root=BuildTree(s)
    print('Recursive Postorder: ',end=" ")
    Postorder(root)
    print()
    print('Morris Postorder: ',end=" ")
    MorrisPostorder(root)
    print()
if __name__=='__main__':
    main()
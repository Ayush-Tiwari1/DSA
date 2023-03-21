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
    size=1
    indx=1
    while size>0 and indx<n:
        temp=dq.popleft()
        size-=1
        if nodes[indx]!='N':
            temp.left=Node(int(nodes[indx]))
            dq.append(temp.left)
            size+=1
        indx+=1
        if indx>=n:
            break
        if nodes[indx]!='N':
            temp.right=Node(int(nodes[indx]))
            dq.append(temp.right)
            size+=1
        indx+=1
    return root

def Inorder(root):
    if root==None:
        return
    Inorder(root.left)
    print(root.data,end=" ")
    Inorder(root.right)

def DeleteTree(root):
    if root==None:
        return
    DeleteTree(root.left)
    DeleteTree(root.right)
    root.left=None
    root.right=None

def Serialize(root,A):
    if root==None:
        return
    dq=deque()
    dq.append(root)
    while len(dq)>0:
        currsize=len(dq)
        for indx in range(currsize):
            temp=dq.popleft()
            if temp!=None:
                A.append(str(temp.data))
                dq.append(temp.left)
                dq.append(temp.right)
            else:
                A.append('N')
    # print(A)
    
def DeSerialize(A):
    n=len(A)
    if n==0 or A[0]=='N':
        return None
    root=Node(int(A[0]))
    dq=deque()
    dq.append(root)
    size=1
    indx=1
    while size>0 and indx<n:
        temp=dq.popleft()
        size-=1
        if A[indx]!='N':
            temp.left=Node(int(A[indx]))
            dq.append(temp.left)
            size+=1
        indx+=1
        if indx>=n:
            break
        if A[indx]!='N':
            temp.right=Node(int(A[indx]))
            dq.append(temp.right)
            size+=1
        indx+=1
    return root

def main():
    s=input()
    root=BuildTree(s)
    print('Before:',end=" ")
    Inorder(root)
    print()
    A=[]
    Serialize(root,A)
    DeleteTree(root)
    root=None
    r=DeSerialize(A)
    print('After:',end=" ")
    Inorder(r)
    print()

if __name__=='__main__':
    main()
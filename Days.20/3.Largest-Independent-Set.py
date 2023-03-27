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

#Include-Exclude Concept
#[Include,Exclude]
def LIS(root):
    if root==None:
        return [0,0]
    l=LIS(root.left)
    r=LIS(root.right)
    if root.left==None and root.right==None:
        return [1,0]
    ans=[]
    ans.append(1+l[1]+r[1])
    max0=max(l[0]+r[0],l[0]+r[1])
    max1=max(l[1]+r[0],l[1]+r[1])
    ans.append(max(max0,max1))
    return ans

def main():
    s=input()
    root=BuildTree(s)
    Inorder(root)
    print()
    ans=LIS(root)
    print('Largest Independent Set:',max(ans[0],ans[1]))

if __name__=='__main__':
    main()
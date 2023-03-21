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

def Inorder(root):
    if root==None:
        return
    Inorder(root.left)
    print(root.data,end=" ")
    Inorder(root.right)

def MaxDifference(root,ans):
    if root==None:
        return 2**63
    if root.left==None and root.right==None:
        return root.data
    left=MaxDifference(root.left,ans)
    right=MaxDifference(root.right,ans)
    mini=min(left,right)
    ans[0]=max(ans[0],root.data-mini)
    return min(mini,root.data)

def main():
    s=input()
    root=BuildTree(s)
    Inorder(root)
    ans=[-2**63]
    MaxDifference(root,ans)
    print('\nMax Difference:',ans[0])


if __name__=='__main__':
    main()
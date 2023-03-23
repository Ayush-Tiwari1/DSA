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

def TargetPath(root,target,ans,nodes):
    if root==None:
        return
    nodes[0].append(root)
    if root.data==target:
        ans[0]=nodes[0][:]
        return
    TargetPath(root.left,target,ans,nodes)
    TargetPath(root.right,target,ans,nodes)
    nodes[0].pop()

def Distance(root,blocker,k,values):
    if root==None:
        return
    if root==blocker:
        return
    if k==0:
        values.append(root.data)
    Distance(root.left,blocker,k-1,values)
    Distance(root.right,blocker,k-1,values)

def NodesKDistanceAway(root,target,k):
    ans=[[]]
    nodes=[[]]
    TargetPath(root,target,ans,nodes)
    path=ans[0]
    path.append(None)
    values=[]
    for indx in range(len(path)-2,-1,-1):
        if k<0:
            break
        Distance(path[indx],path[indx+1],k,values)
        k-=1
    values.sort()
    return values

def main():
    s=input()
    target=int(input())
    k=int(input())
    root=BuildTree(s)
    # Inorder(root)
    # print()
    ans=NodesKDistanceAway(root,target,k)
    print(ans)

if __name__=='__main__':
    main()
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

def NodePath(root,target,arr,nodes):
    if root==None:
        return
    arr.append(root)
    if root.data==target:
        for node in arr:
            nodes.append(node)
        return
    NodePath(root.left,target,arr,nodes)
    NodePath(root.right,target,arr,nodes)
    arr.pop()

def BurnTree(root,blocker,currtime,maxtime):
    if root==None or root==blocker:
        return
    maxtime[0]=max(maxtime[0],currtime)
    BurnTree(root.left,blocker,currtime+1,maxtime)
    BurnTree(root.right,blocker,currtime+1,maxtime)

def BurningTree(root,target):
    nodes=[]
    arr=[]
    NodePath(root,target,arr,nodes)
    # for node in nodes:
    #     print(node.data,end=" ")
    # print()
    time=[0]
    n=len(nodes)
    for indx in range(n-1,-1,-1):
        if indx==n-1:
            blocker=None
        else:
            blocker=nodes[indx+1]
        BurnTree(nodes[indx],blocker,n-indx-1,time)
    return time[0]

def main():
    s=input()
    target=int(input())
    root=BuildTree(s)
    # Inorder(root)
    time=BurningTree(root,target)
    print('Time Required to burn Tree:',time)

if __name__=='__main__':
    main()
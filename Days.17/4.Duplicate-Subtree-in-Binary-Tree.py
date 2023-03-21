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

def DuplicateSubtree(root,dict):
    if root==None:
        return "$"
    l=DuplicateSubtree(root.left,dict)
    r=DuplicateSubtree(root.right,dict)
    ans=l+str(root.data)+r
    if ans in dict:
        dict[ans]+=1
    else:
        dict[ans]=1
    return ans

def main():
    s=input()
    root=BuildTree(s)
    Inorder(root)
    dict={}
    print()
    flag=False
    DuplicateSubtree(root,dict)
    for dic in dict:
        if dict[dic]>1:
            dollar=0
            for char in dic:
                if char=='$':
                    dollar+=1
            if dollar>2:
                flag=True
    if flag==True:
        print('Duplicate Subtree: Present')
    else:
        print('Duplicate Subtree: Not Present')
if __name__=='__main__':
    main()
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
def TopView(root,indx,dict):
    dq=deque()
    dq.append([root,indx])
    size=1
    while size>0:
        temp=dq.popleft()
        size-=1
        if temp[1] not in dict:
            dict[temp[1]]=temp[0].data
        if temp[0].left!=None:
            dq.append([temp[0].left,temp[1]-1])
            size+=1
        if temp[0].right!=None:
            dq.append([temp[0].right,temp[1]+1])
            size+=1
def main():
    s=input()
    root=BuildTree(s)
    Inorder(root)
    dict={}
    TopView(root,0,dict)
    print()
    # dict.sort()
    ans=[]
    for i in dict:
        ans.append([i,dict[i]])
    ans.sort()
    print(ans)
    values=[]
    for i in ans:
        values.append(i[1])
    print(values)

if __name__=='__main__':
    main()
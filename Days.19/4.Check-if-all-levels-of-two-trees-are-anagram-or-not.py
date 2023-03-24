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

def LevelOrder(root):
    dq=deque()
    dq.append(root)
    ans=[]
    while len(dq)>0:
        currsize=len(dq)
        nodes=[]
        for i in range(currsize):
            temp=dq.popleft()
            nodes.append(temp.data)
            if temp.left!=None:
                dq.append(temp.left)
            if temp.right!=None:
                dq.append(temp.right)
        nodes.sort()
        ans.append(nodes)
    return ans

def IsAnagramLevels(root1,root2):
    level1=LevelOrder(root1)
    level2=LevelOrder(root2)
    n1=len(level1)
    n2=len(level2)
    if n1!=n2:
        return 0
    for i in range(n1):
        m1=len(level1[i])
        m2=len(level2[i])
        if m1!=m2:
            return 0
        for j in range(m1):
            if level1[i][j]!=level2[i][j]:
                return 0        
    return 1

def main():
    s1=input()
    s2=input()
    root1=BuildTree(s1)
    root2=BuildTree(s2)
    # Inorder(root1)
    # print()
    # Inorder(root2)
    # print()
    ans=IsAnagramLevels(root1,root2)
    if ans==1:
        print('Anagrams at each Level')
    else:
        print('Anagrams are not possible')

if __name__=='__main__':
    main()
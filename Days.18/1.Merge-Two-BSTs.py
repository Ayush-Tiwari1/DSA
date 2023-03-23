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

def Inorder(root,arr):
    if root==None:
        return
    Inorder(root.left,arr)
    arr.append(root.data)
    Inorder(root.right,arr)
def Inorder1(root):
    if root==None:
        return
    Inorder1(root.left)
    print(root.data,end=" ")
    Inorder1(root.right)
def Merge2SortedArray(arr1,arr2):
    indx1=0
    indx2=0
    size1=len(arr1)
    size2=len(arr2)
    ans=[]
    while indx1<size1 and indx2<size2:
        if arr1[indx1]<arr2[indx2]:
            ans.append(arr1[indx1])
            indx1+=1
        else:
            ans.append(arr2[indx2])
            indx2+=1
    while indx1<size1:
        ans.append(arr1[indx1])
        indx1+=1
    while indx2<size2:
        ans.append(arr2[indx2])
        indx2+=1
    return ans

def ArraytoBST(arr,start,end):
    if start>end:
        return None
    n=(start+end)//2
    root=Node(arr[n])
    root.left=ArraytoBST(arr,start,n-1)
    root.right=ArraytoBST(arr,n+1,end)
    return root
def main():
    s1=input()
    s2=input()
    root1=BuildTree(s1)
    root2=BuildTree(s2)
    arr1=[]
    Inorder(root1,arr1)
    # print(arr1)
    arr2=[]
    Inorder(root2,arr2)
    # print(arr2)
    ans=Merge2SortedArray(arr1,arr2)
    print(ans)
    root=ArraytoBST(ans,0,len(ans)-1)
    Inorder1(root)
if __name__=='__main__':
    main()
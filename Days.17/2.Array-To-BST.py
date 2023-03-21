
class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

def ArraytoBST(s,start,end):
    if start>end:
        return None
    n=(start+end)//2
    root=Node(s[n])
    root.left=ArraytoBST(s,start,n-1)
    root.right=ArraytoBST(s,n+1,end)
    return root

def Inorder(root):
    if root==None:
        return
    Inorder(root.left)
    print(root.data,end=" ")
    Inorder(root.right)

def main():
    s=list(map(int,input().split()))
    root=ArraytoBST(s,0,len(s)-1)
    Inorder(root)


if __name__=='__main__':
    main()
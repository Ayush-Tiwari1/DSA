
class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
        self.height=1
def getHeight(root):
    if root==None:
        return 0
    return root.height

def getBalanceFactor(root):
    if root==None:
        return 0
    return getHeight(root.left)-getHeight(root.right)


def RightRotate(root):
    z=root
    y=root.left
    t3=root.left.right
    y.right=z
    z.left=t3
    z.height=1+max(getHeight(z.left),getHeight(z.right))
    y.height=1+max(getHeight(y.left),getHeight(y.right))
    return y

def LeftRotate(root):
    x=root
    y=root.right
    t2=root.right.left
    y.left=x
    x.right=t2
    x.height=1+max(getHeight(x.left),getHeight(x.right))
    y.height=1+max(getHeight(y.left),getHeight(y.right))
    return y

def AVLTree(root,key):
    if root==None:
        return Node(key)
    elif root.data==key:
        return root
    elif root.data>key:
        root.left=AVLTree(root.left,key)
    else:
        root.right=AVLTree(root.right,key)
    root.height=1+max(getHeight(root.left),getHeight(root.right))
    balance=getBalanceFactor(root)
    #LL Case-->RightRotate()
    if balance>1 and root.left.data>key:
        return RightRotate(root)
    #LR Case-->root.left-->LeftRotate() then root-->RightRotate()
    elif balance>1 and root.left.data<key:
        root.left=LeftRotate(root.left)
        return RightRotate(root)
    #RR Case-->LeftRotate()
    elif balance<-1 and root.right.data<key:
        return LeftRotate(root)
    #RL Case-->root.right-->RightRotate() and root-->LeftRotate()
    elif balance<-1 and root.right.data>key:
        root.right=RightRotate(root.right)
        return LeftRotate(root)
    return root

def Inorder(root):
    if root==None:
        return
    Inorder(root.left)
    print(root.data,end=" ")
    Inorder(root.right)

def main():
    n=int(input())
    values=list(map(int,input().split()))
    root=None
    for i in range(n):
        root=AVLTree(root,values[i])
    Inorder(root)


if __name__=='__main__':
    main()
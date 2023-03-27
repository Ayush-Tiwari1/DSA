
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

def BalanceFactor(root):
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

def Insert(root,key):
    if root==None:
        return Node(key)
    elif root.data==key:
        return root
    elif root.data>key:
        root.left=Insert(root.left,key)
    else:
        root.right=Insert(root.right,key)
    root.height=1+max(getHeight(root.left),getHeight(root.right))
    balance=BalanceFactor(root)
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

def Delete(root,key):
    if root==None:
        return None
    elif root.data>key:
        root.left=Delete(root.left,key)
    elif root.data<key:
        root.right=Delete(root.right,key)
    else:
        if root.left==None:
            return root.right
        elif root.right==None:
            return root.left
        else:
            temp=root.left
            while temp.right!=None:
                temp=temp.right
            root.data=temp.data 
            root.left=Delete(root.left,temp.data)
    root.height=1+max(getHeight(root.left),getHeight(root.right))
    balance=BalanceFactor(root)
    #LL Case-->RightRotate()
    if balance>1 and BalanceFactor(root.left)>=0:
        return RightRotate(root)
    #LR Case-->root.left-->LeftRotate() and root-->RightRotate()
    elif balance>1 and BalanceFactor(root.left)<0:
        root.left=LeftRotate(root.left)
        return RightRotate(root)
    #RR Case-->LeftRotate()
    elif balance<-1 and BalanceFactor(root.right)<=0:
        return LeftRotate(root)
    #RL Case-->root.right-->RightRotate() and root-->LeftRotate()
    elif balance<-1 and BalanceFactor(root.right)>0:
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
        root=Insert(root,values[i])
    Inorder(root)
    print()
    # root=Delete(root,20)
    # Inorder(root)
    # print()


if __name__=='__main__':
    main()
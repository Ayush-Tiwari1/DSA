INT_MIN=-2**63
INT_MAX=2**63-1

class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

def PreorderToBST(pre,indx,n,minimum,maximum):
    if indx[0]>=n:
        return None
    if pre[indx[0]]>maximum or pre[indx[0]]<minimum:
        return None
    root=Node(pre[indx[0]])
    # start+=1
    indx[0]+=1
    root.left=PreorderToBST(pre,indx,n,minimum,root.data)
    root.right=PreorderToBST(pre,indx,n,root.data,maximum)
    return root

def PostOrder(root):
    if root==None:
        return
    PostOrder(root.left)
    PostOrder(root.right)
    print(root.data,end=" ")    

def main():
    pre=list(map(int,input().split()))
    # print(pre)
    indx=[0]
    # print(indx,type(indx[0]))
    root=PreorderToBST(pre,indx,len(pre),INT_MIN,INT_MAX)
    PostOrder(root)


if __name__=='__main__':
    main()
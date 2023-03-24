
class TNode:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

class LNode:
    def __init__(self,data):
        self.data=data
        self.next=None

def LinkedList(list,n):
    head=LNode(list[0])
    temp=head
    for i in range(1,n):
        temp.next=LNode(list[i])
        temp=temp.next
    return head

def SortedLinkedListToBST(head,n):
    if n<=0:
        return None
    l=SortedLinkedListToBST(head,n//2)
    root=TNode(head[0].data)
    head[0]=head[0].next 
    root.left=l
    root.right=SortedLinkedListToBST(head,n-n//2-1)
    return root

def Inorder(root):
    if root==None:
        return
    Inorder(root.left)
    print(root.data,end=" ")
    Inorder(root.right)

def main():
    n=int(input())
    list1=list(map(int,input().split()))
    head=LinkedList(list1,n)
    temp=[head]
    root=SortedLinkedListToBST(temp,n)
    Inorder(root)
if __name__=='__main__':
    main()
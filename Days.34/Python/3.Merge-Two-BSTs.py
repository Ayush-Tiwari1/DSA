# Merge Two BSTs

# Algorithm:
# 1. Convert Two BST ----> Doubly Linked List
# 2. Merge Two DLL
# 3. Convert DLL ---> BST

from collections import deque

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def BuildBST(str):
    n=len(str)
    if n==0 or str[0]=="N":
        return None
    dq=deque()
    root=Node(int(str[0]))
    dq.append(root)
    i=1
    while i<n and dq:
        curr=dq.popleft()
        if str[i]!="N":
            curr.left=Node(int(str[i]))
            dq.append(curr.left)
        i+=1
        if i>=n:
            break
        if str[i]!="N":
            curr.right=Node(int(str[i]))
            dq.append(curr.right)
        i+=1
    return root

def Inorder(root):
    if root==None:
        return
    Inorder(root.left)
    print(root.val,end=" ")
    Inorder(root.right)

def BSTtoDLL(root):
    head=Node(-1)
    temp=head
    curr=root
    
    #Morris Inorder Traversal
    while curr!=None:
        if curr.left==None:
            temp.right=curr
            curr.left=temp
            temp=curr
            curr=curr.right
        else:
            t=curr.left
            while t.right!=None and t.right!=curr:
                t=t.right
            if t.right==None:
                t.right=curr
                curr=curr.left
            else:
                t.right=None
                temp.right=curr
                curr.left=temp
                temp=curr
                curr=curr.right
    head=head.right
    head.left=None
    return head

def PrintDLL(root):
    head=root
    tail=None
    print('Left to Right')
    while head!=None:
        print(head.val,end= " ")
        tail=head
        head=head.right
    print('\nRight to Left')
    while tail!=None:
        print(tail.val,end=" ")
        tail=tail.left
    print()

def MergeDLL(head1, head2):
    head=Node(-1)
    temp=head
    while head1 and head2:
        if head1.val<head2.val:
            temp.right=head1
            head1.left=temp
            temp=head1
            head1=head1.right
        else:
            temp.right=head2
            head2.left=temp
            temp=head2
            head2=head2.right
    if head1:
        temp.right=head1
        head1.left=temp
    if head2:
        temp.right=head2
        head2.left=temp
    head=head.right
    head.left=None
    return head

def LengthofDLL(head):
    temp=head
    count=0
    while temp!=None:
        count+=1
        temp=temp.right
    return count

def DLLtoBST(n,head):
    if head==None or n<=0:
        return None
    left=DLLtoBST(n//2,head)
    root=Node(head[0].val)
    head[0]=head[0].right
    root.left=left
    root.right=DLLtoBST(n-n//2-1,head)
    return root

def MergeTwoBST(root1,root2):

    # 1. BST ----> DLL
    head1=BSTtoDLL(root1)
    head2=BSTtoDLL(root2)
    
    # 2. Merge DLL
    head=MergeDLL(head1,head2)

    # 3. DLL ---> BST
    n=LengthofDLL(head)
    h=[head]
    root=DLLtoBST(n,h)
    return root

def main():
    str1=input().split()
    str2=input().split()
    root1=BuildBST(str1)
    root2=BuildBST(str2)    

    # Inorder(root1)
    # print()
    # Inorder(root2)
    root=MergeTwoBST(root1,root2)
    Inorder(root)



main()
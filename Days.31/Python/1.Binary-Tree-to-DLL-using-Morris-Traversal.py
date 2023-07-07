# Binary Tree to Doubly Linked List using Morris Traversal

from queue import Queue

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def BuildTree(nodes):
    n=len(nodes)
    if n==0 or nodes[0]=='N':
        return None
    q=Queue()
    root=Node(int(nodes[0]))
    q.put(root)
    i=1
    while i<n and q.empty()==False:
        curr=q.get()
        # Left Child
        if nodes[i]!='N':
            curr.left=Node(int(nodes[i]))
            q.put(curr.left)
        i+=1
        if i>=n:
            break
        if nodes[i]!='N':
            curr.right=Node(int(nodes[i]))
            q.put(curr.right)
        i+=1
    return root

def Inorder(root):
    if root==None:
        return
    Inorder(root.left)
    print(root.val,end=" ")
    Inorder(root.right)

def BTtoDLL(root):
    head=tail=Node(-1)
    temp=head

    curr=root
    while curr!=None:
        if curr.left==None:
            temp.right=curr
            curr.left=temp
            temp=curr
            tail=temp
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
                tail=temp
                curr=curr.right
    head=head.right
    head.left=None
    return head,tail

def printHead(head):
    curr=head
    while curr!=None:
        print(curr.val,end=" ")
        curr=curr.right
    print()

def printTail(tail):
    curr=tail
    while tail!=None:
        print(tail.val,end=" ")
        tail=tail.left
    print()

def main():
    nodes=input().split()
    root=BuildTree(nodes)
    # Inorder(root)
    head,tail=BTtoDLL(root)
    printHead(head)
    printTail(tail)
main()


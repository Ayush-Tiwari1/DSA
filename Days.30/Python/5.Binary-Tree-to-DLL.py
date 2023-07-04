# Binary Tree to Doubly Linked List
from queue import Queue

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def BuildTree(str):
    n=len(str)
    if n==0 or str[0]=='N':
        return None
    root=Node(int(str[0]))
    i=1
    q=Queue()
    q.put(root)
    while q.empty()==False and i<n:
        curr=q.get()
        #Left Child
        if str[i]!='N':
            curr.left=Node(int(str[i]))
            q.put(curr.left)
        i+=1
        if i>=n:
            break
        
        #Right Child
        if str[i]!='N':
            curr.right=Node(int(str[i]))
            q.put(curr.right)
        i+=1
    return root

def Preorder(root):
    if root==None:
        return
    Preorder(root.left)
    print(root.val,end=" ")
    Preorder(root.right)

def BTtoDLL(temp,root):
    if root==None:
        return
    BTtoDLL(temp,root.left)
    temp[0].right=root
    root.left=temp[0]
    temp[0]=temp[0].right
    BTtoDLL(temp,root.right)
    

def printhead(head):
    curr=head
    while curr!=None:
        print(curr.val,end=" ")
        curr=curr.right
    print()

def printtail(tail):
    curr=tail
    while curr!=None:
        print(curr.val,end=" ")
        curr=curr.left
    print()

def main():
    str=input().split()
    root=BuildTree(str)
    # Preorder(root)
    head=Node(-1)
    temp=[head]
    BTtoDLL(temp,root)
    head=head.right
    head.left=None
    first=last=head
    while last.right!=None:
        last=last.right
    print('Print Head: ',end="")
    printhead(first)
    print('Print Tail: ',end="")
    printtail(last)

main()


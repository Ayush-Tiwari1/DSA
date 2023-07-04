

class Node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def InsertEnd(self,val):
        if self.head==None:
            self.head=self.tail=Node(val)
        else:
            temp=Node(val)
            self.tail.next=temp
            temp.prev=self.tail
            self.tail=temp
    
    def DeleteEnd(self):
        if self.head==None:
            return -1
        else:
            prev=None
            curr=self.head
            while curr!=self.tail:
                prev=curr
                curr=curr.next
            val=curr.val
            curr.prev=None
            prev.next=None
            self.tail=prev
            return val


def printDLL(head):
    curr=head
    while curr!=None:
        print(curr.val,end=" ")
        curr=curr.next
    print()

def Split(head):
    slow=fast=head
    prev=None
    while fast.next!=None and fast.next.next!=None:
        slow=slow.next
        prev=fast
        fast=fast.next.next
    head1=head
    head2=slow.next
    slow.next=None
    return head1,head2

def Merge(head1,head2):
    head=Node(-1)
    temp=head
    while head1!=None and head2!=None:
        if head1.val<head2.val:
            temp.next=head1
            head1.prev=temp
            head1=head1.next
        else:
            temp.next=head2
            head2.prev=temp
            head2=head2.next 
        temp=temp.next
    if head1!=None:
        temp.next=head1
        head1.prev=temp
    if head2!=None:
        temp.next=head2
        head2.prev=temp
    head=head.next
    head.prev=None
    return head

def MergeSort(head):
    if head.next==None:
        return head
    head1,head2=Split(head)
    h1=MergeSort(head1)
    h2=MergeSort(head2)
    return Merge(h1,h2)

def main():
    n=int(input())
    values=input().split()
    dll=DoublyLinkedList()
    for val in values:
        dll.InsertEnd(int(val))
    print('Before Merge Sort:')
    printDLL(dll.head)
    dll.head=MergeSort(dll.head)
    print('After Merge Sort')
    printDLL(dll.head)


main()


# Doubly Linked List 

class Node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def size(self):
        sz=0
        temp=self.head
        while temp!=None:
            sz+=1
            temp=temp.next
        return sz

    def InsertBegin(self,val):
        temp=Node(val)
        if self.head==None:
            self.head=self.tail=temp
        else:
            self.head.prev=temp
            temp.next=self.head
            self.head=temp
    
    def InsertEnd(self,val):
        temp=Node(val)
        if self.head==None:
            self.head=self.tail=temp
        else:
            self.tail.next=temp
            temp.prev=self.tail
            self.tail=self.tail.next

    def InsertPosition(self,val,pos):
        n=self.size()
        if pos<0 or pos>n:
            print('Index Out of Bound')
        else:
            if pos==0:
                self.InsertBegin(val)
            elif pos==n:
                self.InsertEnd(val)
            else:
                temp=Node(val)
                i=1
                curr=self.head
                while i!=pos:
                    i+=1
                    curr=curr.next
                temp.next=curr.next
                if curr.next!=None:
                    curr.next.prev=temp
                temp.prev=curr
                curr.next=temp

    def DeleteBegin(self):
        if self.head==None:
            return -1
        else:
            if self.head.next==None:
                val=self.head.val
                self.head=self.tail=None
                return val
            else:
                val=self.head.val
                self.head=self.head.next
                self.head.prev=None
                return val
        
    def DeleteEnd(self):
        if self.head==None:
            return -1
        else:
            if self.head.next==None:
                val=self.head.val
                self.head=self.tail=None
                return val
            else:
                val=self.tail.val
                prev=self.tail.prev
                prev.next=None
                self.tail=prev
                return val
    
    def DeletePosition(self,pos):
        if self.head==None:
            return -1
        else:
            n=self.size()
            if pos<0 or pos>n:
                return -1
            if pos==1:
                return self.DeleteBegin()
            elif pos==n:
                return self.DeleteEnd()
            else:
                i=1
                curr=self.head
                while i!=pos:
                    i+=1
                    curr=curr.next
                val=curr.val
                curr.prev.next=curr.next
                curr.next.prev=curr.prev
                return val

    def Middle(self):
        slow=fast=self.head
        if slow==None:
            return -1
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow.val

    def printDoublyLinkedList(self):
        temp=self.head
        if temp==None:
            print('Doubly Linked List is Empty')
        else:
            while temp!=None:
                print(temp.val,end=" ")
                temp=temp.next
            print()


def main():
    doublylinkedlist=DoublyLinkedList()
    while True:
        print('1.Insert at the Beginning')
        print('2.Insert at the End')
        print('3.Insert at the Given Postition')
        print('4.Delete at the Beginning')
        print('5.Delete at the End')
        print('6.Delete at the Given Position')
        print('7.Size of Doubly Linked List')
        print('8.Middle of the Doubly Linked List')
        print('9.Print Doubly Linked List')
        print('10.Exit')
        choice=int(input('Enter Your Choice:\t'))
        if choice==1:
            val=int(input('Enter a Value: '))
            doublylinkedlist.InsertBegin(val)
        elif choice==2:
            val=int(input('Enter a Value: '))
            doublylinkedlist.InsertEnd(val)
        elif choice==3:
            val=int(input('Enter a Value: '))
            pos=int(input('Enter a Position: '))
            doublylinkedlist.InsertPosition(val,pos)
        elif choice==4:
            val=doublylinkedlist.DeleteBegin()
            if val==-1:
                print('Doubly Linked List is Empty')
            else:
                print('Deleted Value:',val)
        elif choice==5:
            val=doublylinkedlist.DeleteEnd()
            if val==-1:
                print('Doubly Linked List is Empty')
            else:
                print('Deleted Value:',val)
        elif choice==6:
            pos=int(input('Enter a Position: '))
            val=doublylinkedlist.DeletePosition(pos)
            if val==-1:
                print('Index Out of Bound')
            else:
                print('Deleted Value at Position',pos,':',val)
        elif choice==7:
            print('Size:',doublylinkedlist.size())
        elif choice==8:
            val=doublylinkedlist.Middle()
            if val==-1:
                print('Doubly Linked List is Empty')
            else:
                print('Middle of the Doubly Linked List:',val)
        elif choice==9:
            doublylinkedlist.printDoublyLinkedList()
        elif choice==10:
            break
        else:
            print('Invalid Choice')

main()




class Node:
    def __init__(self,val=-1):
        self.val=val
        self.next=None
class LinkedList:

    def __init__(self):
        self.head=None
        self.tail=None

    def InsertEnd(self,val):
        if self.head==None:
            self.head=self.tail=Node(val)
        else:
            self.tail.next=Node(val)
            self.tail=self.tail.next

    def InsertBegin(self,val):
        if self.head==None:
            self.head= self.tail =Node(val)
        else:
            temp=Node(val)
            temp.next=self.head
            self.head=temp

    def InsertPosition(self,val,pos):
        #Pos ----> Based on 1-Based Indexing
        n=self.size()
        if pos<0 or pos>n+1:
            print('Index Out of Bound')
            return
        else:
            if pos==1:
                self.InsertBegin(val)
            elif pos==n+1:
                self.InsertEnd(val)
            else:
                prev=None
                curr=self.head
                i=1
                while i!=pos:
                    prev=curr
                    curr=curr.next
                    i+=1
                temp=Node(val)
                temp.next=curr
                prev.next=temp

        
    def DeletionEnd(self):
        if self.head==None:
            return -1
        if self.head.next==None:
            val=self.head.val
            self.head=self.tail=None
            return val
        else:
            temp=self.head
            prev=None
            while temp.next!=None:
                prev=temp
                temp=temp.next
            val=temp.val
            prev.next=None
            return val
        
    def DeletionBegin(self):
        if self.head==None:
            return -1
        if self.head.next==None:
            val=self.head.val
            self.head=tail=None
            return val
        val=self.head.val
        self.head=self.head.next 
        return val
        
    def DeletionPosition(self,pos):
        if self.head==None:
            return -1
        if pos<0 or pos>self.size():
            return -1
        if pos==1:
            return self.DeletionBegin()
        elif pos==self.size():
            return self.DeletionEnd()
        else:
            i=1
            prev=None
            curr=self.head
            while i!=pos:
                prev=curr
                curr=curr.next
                i+=1
            val=curr.val
            prev.next=curr.next 
            return val

    def size(self):
        sz=0
        temp=self.head
        while temp!=None:
            sz+=1
            temp=temp.next
        return sz

def main():
    linkedlist=LinkedList()
    while True:
        print('1.Insert at the End')
        print('2.Insert at the Beginning')
        print('3.Insert at Given Position')
        print('4.Deletion at the End')
        print('5.Deletion at the Beginning')
        print('6.Deletion at Given Position')
        print('7.Size of Linked List')
        print('8.Print')
        print('9.Exit')
        choice=int(input('Enter Your Choice: '))
        if choice==1:
            val=int(input('Enter a Value: '))
            linkedlist.InsertEnd(val)
        
        elif choice==2:
            val=int(input('Enter a Value: '))
            linkedlist.InsertBegin(val)
        
        elif choice==3:
            val=int(input('Enter a Value: '))
            pos=int(input('Enter a Position: '))
            linkedlist.InsertPosition(val,pos)
        
        elif choice==4:
            val=linkedlist.DeletionEnd()
            if val==-1:
                print('Linked List is Empty')
            else:
                print('Deleted Value:',val)
        
        elif choice==5:
            val=linkedlist.DeletionBegin()
            if val==-1:
                print('Linked List is Empty')
            else:
                print('Deleted Value:',val)
        
        elif choice==6:
            pos=int(input('Enter a Position: '))
            val=linkedlist.DeletionPosition(pos)
            if val==-1:
                print('Index Out of Bound')
            else:
                print('Deleted Value:',val)
        
        elif choice==7:
            print('Size:',linkedlist.size())

        elif choice==8:
            if linkedlist.head==None:
                print('Linked List is Empty')
            else:
                temp=linkedlist.head
                while temp!=None:
                    print(temp.val,end=" ")
                    temp=temp.next
                print()
        elif choice==9:
            break
        else:
            print('Invalid Choice')
    

main()


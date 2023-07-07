# Reverse a Doubly Linked List in a group of given size k

class Node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None

class DLL:
    def __init__(self):
        self.head=self.tail=None
    def Insert(self,val):
        if self.head==None:
            self.head=self.tail=Node(val)
        else:
            temp=Node(val)
            self.tail.next=temp
            temp.prev=self.tail
            self.tail=temp 
    '''
    ///Concept: Reverse a Linked List using AddFirst 
        struct node *th,*tt,*oh,*ot;
        oh=ot=th=th=NULL;
        int count;
        struct node *c,*f;
        c=head;
        count=k;
        while(c!=NULL)
        {
            f=c->next;
            if(th==NULL)
            {
                th=tt=c;
                c->next=NULL;
            }
            else
            {
                c->next=th;
                th=c;
            }
                count--;
            if(count==0)
            {
                if(oh==NULL)
                {
                    oh=th;
                    ot=tt;
                    th=tt=NULL;
                }
                else
                {
                    ot->next=th;
                    ot=tt;
                    th=tt=NULL;
                }
                count=k;
            }
            c=f;
        }
        if(th!=NULL)
        {
            ot->next=th;
            ot=tt;
        }
        return oh;
    '''
    def Reverse(self, k):
        oh=ot=None
        th=tt=None
        count=0
        curr=self.head
        next=None
        while curr!=None:
            next=curr.next
            if count==k:
                if oh==None:
                    oh=th
                    ot=tt
                else:
                    ot.next=th
                    th.prev=ot
                    ot=tt
                th=tt=None
                count=0
            else:
                if th==None:
                    curr.prev=curr.next=None
                    th=tt=curr
                else:
                    curr.next=th
                    th.prev=curr
                    curr.prev=None
                    th=curr
                count+=1
                curr=next
        if th!=None:
            ot.next=th
            th.prev=ot
            ot=tt
        self.head=oh
        self.tail=ot

    def printHead(self):
        curr=self.head
        while curr!=None:
            print(curr.val,end=" ")
            curr=curr.next
        print()
    def printTail(self):
        curr=self.tail
        while curr!=None:
            print(curr.val,end=" ")
            curr=curr.prev
        print()
    

def main():
    nodes=input().split()
    k=int(input())
    dll=DLL()
    for node in nodes:
        dll.Insert(int(node))
    dll.printHead()
    dll.printTail()
    dll.Reverse(k)
    dll.printHead()
    dll.printTail()


main()


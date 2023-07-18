
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
    def Insert(self,root,val):
        if root==None:
            return Node(val)
        if root.val==val:
            return root
        elif root.val>val:
            root.left=self.Insert(root.left,val)
        else:
            root.right=self.Insert(root.right,val)
        return root
    
    def Search(self,root,val):
        if root==None:
            return False
        if root.val==val:
            return True
        if root.val>val:
            return self.Search(root.left,val)
        else:
            return self.Search(root.right,val)

    def Delete(self,root,val):
        if root==None:
            return None
        if root.val==val:
            if root.left==None and root.right==None:
                return None
            elif root.left!=None and root.right!=None:
                temp=root.left
                while temp.right!=None:
                    temp=temp.right
                root.val=temp.val
                root.left= self.Delete(root.left,temp.val)
                return root
            elif root.left!=None:
                return root.left
            else:
                return root.right
        if root.val>val:
            root.left= self.Delete(root.left,val)
        else:
            root.right=self.Delete(root.right,val)
        return root

    def Inorder(self,root):
        if root==None:
            return
        self.Inorder(root.left)
        print(root.val,end=" ")
        self.Inorder(root.right)


def main():
    bst=BST()
    while True:
        print('1.Insert')
        print('2.Delete')
        print('3.Search')
        print('4.Inorder Traversal')
        print('5.Exit')
        choice=int(input('Enter Your Choice: '))
        if choice==1:
            val=int(input('Enter a Value: '))
            bst.root=bst.Insert(bst.root,val)
        elif choice==2:
            val=int(input('Enter Value to be Deleted: '))
            flag=False
            if bst.Search(bst.root,val):
                flag=True
                bst.root=bst.Delete(bst.root,val)
            if flag:
                print('Deleted Successfully')
            else:
                print('Value is Not Present in BST')
        elif choice==3:
            val=int(input('Enter value for searching: '))
            if bst.Search(bst.root,val):
                print('Present in BST')
            else:
                print('Not Present in BST')
        elif choice==4:
            bst.Inorder(bst.root)
            print()
        elif choice==5:
            break
        else:
            print('Invalid Choice')



main()


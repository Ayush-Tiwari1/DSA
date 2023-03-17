from collections import deque
class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

class Tree:
    def BuildTree(self,s):
        nodes=s.split()
        n=len(nodes)
        if n==0 or nodes[0]=='N':
            return None
        root=Node(int(nodes[0]))
        dq=deque()
        dq.append(root)
        size=1
        i=1
        while size>0 and i<n:
            temp=dq.popleft()
            size-=1
            if nodes[i]!='N':
                temp.left=Node(int(nodes[i]))
                dq.append(temp.left)
                size+=1
            i+=1
            if i>=n:
                break
            if nodes[i]!='N':
                temp.right=Node(int(nodes[i]))
                dq.append(temp.right)
                size+=1
            i+=1
        return root
    def Inorder(self,root):
        if root==None:
            return
        self.Inorder(root.left)
        print(root.data,end=" ")
        self.Inorder(root.right)
    def helper(self,root,indx,dict):
        if root==None:
            return
        if indx not in dict:
            dict[indx]=[root.data]
        else:
            dict[indx].append(root.data)
        self.helper(root.left,indx-1,dict)
        self.helper(root.right,indx+1,dict)
    def VerticalOrder(self,root):
        diction={}
        self.helper(root,0,diction)
        sorted_dict=dict(sorted(diction.items()))
        print(sorted_dict)
        ans=[]
        for i in sorted_dict:
            # print(sorted_dict[i])
            temp=sorted_dict[i]
            for val in temp:
                ans.append(val)
        return ans
def main():
    s=input()
    tree=Tree()
    root=tree.BuildTree(s)
    tree.Inorder(root)
    ans=tree.VerticalOrder(root)
    print(ans)
    

if __name__=='__main__':
    main()
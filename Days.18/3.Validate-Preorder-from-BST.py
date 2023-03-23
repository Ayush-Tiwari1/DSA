
def CheckBST(pre,preindx,n,mini,maxi):
    if preindx[0]>=n:
        return
    if pre[preindx[0]]>mini and pre[preindx[0]]<maxi:
        rootdata=pre[preindx[0]]
        preindx[0]+=1
        CheckBST(pre,preindx,n,mini,rootdata)
        CheckBST(pre,preindx,n,rootdata,maxi)

def ValidatePreorder(pre,n):
    preindx=[0]
    CheckBST(pre,preindx,n,-2**63,2**63)
    if preindx[0]==n:
        return 1
    return 0
def main():
    n=int(input())
    pre=list(map(int,input().split()))
    ans=ValidatePreorder(pre,n)
    if ans==1:
        print('Preorder of BST')
    else:
        print('Not Preorder of BST')


if __name__=='__main__':
    main()
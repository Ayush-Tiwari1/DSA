# Tower of Hanoi

def TOH(n,beg,aux,end):
    if n<=0:
        return
    TOH(n-1,beg,end,aux)
    print(beg,'->',end)
    TOH(n-1,aux,beg,end)



def main():
    n=int(input())
    TOH(n,'A','B','C')



if __name__=='__main__':
    main()
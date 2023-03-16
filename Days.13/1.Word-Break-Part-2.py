

def main():
    def Solve(n,d,s):
        def WordBreak(indx,n,dict,s,curr,ans):
            if indx==n:
                ans.append(curr)
                return
            str=""
            for i in range(indx,n):
                str+=s[i]
                if str in dict:
                    ch=''
                    if i+1 !=n:
                        ch=' '
                    WordBreak(i+1,n,dict,s,curr+str+ch,ans)
        dict={}
        for i in range(n):
            dict[d[i]]=True
        ans=[]
        WordBreak(0,len(s),dict,s,"",ans)
        return ans
    t=int(input())
    for _ in range(t):
        n=int(input())
        d=list(input().split())
        s=input()
        ans=Solve(n,d,s)
        print(ans)

if __name__=='__main__':
    main()



def main():
    def BooleanParenthesization(n,str):
        s1=''
        s2=''
        for i in range(n):
            if str[i]=='T' or str[i]=='F':
                s1+=str[i]
            else:
                s2+=str[i]
        n=len(s1)
        truedp=[[0]*n for i in range(n)]
        falsedp=[[0]*n for i in range(n)]
        #Gape Strategy
        for g in range(0,n):
            for i,j in zip(range(0,n),range(g,n)):
                if g==0:
                    if s1[i]=='T':
                        truedp[i][j]=1
                        falsedp[i][j]=0
                    else:
                        truedp[i][j]=0
                        falsedp[i][j]=1
                elif g==1:
                    if s2[i]=='&':
                        if s1[i]=='T' and s1[j]=='T':
                            truedp[i][j]=1
                            falsedp[i][j]=0
                        else:
                            truedp[i][j]=0
                            falsedp[i][j]=1
                    elif s2[i]=='|':
                        if s1[i]=='T' or s1[j]=='T':
                            truedp[i][j]=1
                            falsedp[i][j]=0
                        else:
                            truedp[i][j]=0
                            falsedp[i][j]=1
                    else:
                        if (s1[i]=='T' and s1[j]=='T') or (s1[i]=='F' and s1[j]=='F'):
                            truedp[i][j]=0
                            falsedp[i][j]=1
                        else:
                            truedp[i][j]=1
                            falsedp[i][j]=0
                else:
                    
                    for k in range(i,j):
                        ltc=truedp[i][k]
                        rtc=truedp[k+1][j]
                        lfc=falsedp[i][k]
                        rfc=falsedp[k+1][j]
                        if s2[k]=='&':
                            truedp[i][j]+=ltc*rtc
                            falsedp[i][j]+=ltc*rfc+lfc*rtc+lfc*rfc
                        elif s2[k]=='|':
                            truedp[i][j]+=ltc*rtc+ltc*rfc+lfc*rtc
                            falsedp[i][j]+=lfc*rfc
                        else:
                            truedp[i][j]+=ltc*rfc+lfc*rtc
                            falsedp[i][j]+=ltc*rtc+lfc*rfc
        # print(truedp)
        # print(falsedp)
        return truedp[0][n-1]
        
    n=int(input())
    str=input()
    ans=BooleanParenthesization(n,str)
    print(ans)

if __name__=='__main__':
    main()
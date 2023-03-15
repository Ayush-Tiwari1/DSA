
class Solution:
    def multiplyStrings(self,s1,s2):
        if s1=='0' or s2=='0':
            return '0'
        neg=False
        if s1[0]=='-' and s2[0]=='-':
            neg=False
        elif s1[0]=='-' or s2[0]=='-':
            neg=True
        if s1[0]=='-':
            s1=s1[1:]
        if s2[0]=='-':
            s2=s2[1:]
        n1=len(s1)
        n2=len(s2)
        ans=[]
        for i in range(n1+n2):
            ans.append(0)
        k=0
        prod=0
        res=0
        carry=0
        for i in range(n1-1,-1,-1):
            p=k
            num1=int(s1[i])
            for j in range(n2-1,-1,-1):
                num2=int(s2[j])
                prod=num1*num2+ans[p]+carry
                res=prod%10
                carry=int(prod/10)
                ans[p]=res
                p+=1
            if carry!=0:
                ans[p]=ans[p]+carry
                carry=0
            k+=1
        temp=""
        if neg==True:
            temp+="-"
        flag=False
        for i in range(n1+n2-1,-1,-1):
            if ans[i]!=0:
                flag=True
            if flag == True:
                temp+=str(ans[i])
                
        return temp


if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        a,b=input().split()
        print(Solution().multiplyStrings( a.strip() , b.strip() ))

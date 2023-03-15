#Convert String to Integer
#without str()
class Solution:

    def atoi(self,string):
        ans=0
        neg=False
        if string[0]=='-':
            neg=True
            string=string[1:]
            
        #ord(character)====> gives ascii value of character
        for i in range(len(string)):
            if string[i]>='0' and string[i]<='9':
                ans=ans*10+(ord(string[i])-ord('0'))
            else:
                return -1
        if neg==True:
            ans=-ans
        return ans


if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
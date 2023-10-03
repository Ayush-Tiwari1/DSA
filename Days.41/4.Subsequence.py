# Get Subsequence

# Include Exclude Concept

def GetSubsequence(indx,string,ans):
    if indx==len(string):
        print(ans)
        return
    GetSubsequence(indx+1,string,ans)
    GetSubsequence(indx+1,string,ans+string[indx])



def main():
    string=input()
    GetSubsequence(0,string,"")



if __name__=="__main__":
    main()
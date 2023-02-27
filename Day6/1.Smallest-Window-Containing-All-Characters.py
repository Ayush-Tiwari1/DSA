

def main():
    def SmallestWindow(S,P):
        mainhash={}
        n=len(P)
        for i in range(n):
            if P[i] not in mainhash:
                mainhash[P[i]]=1
            else:
                mainhash[P[i]]+=1
        currhash={}
        count=0
        i=j=0
        ans=''
        while j<len(S):
            while count<n and j<len(S):
                if S[j] in mainhash:
                    if S[j] not in currhash:
                        currhash[S[j]]=1
                        count+=1
                    elif currhash[S[j]]<mainhash[S[j]]:
                        currhash[S[j]]+=1
                        count+=1
                    else:
                        currhash[S[j]]+=1
                else:
                    if S[j] not in currhash:
                        currhash[S[j]]=1
                    else:
                        currhash[S[j]]+=1
                j+=1
            while count==n and i<j:
                # print(S[i:j])
                if len(ans)==0:
                    ans=S[i:j]
                elif len(ans)> len(S[i:j]):
                    ans=S[i:j]
                currhash[S[i]]-=1
                if S[i] in mainhash and currhash[S[i]]<mainhash[S[i]]:
                    count-=1
                i+=1
        while count==n and i<j:
            # print(S[i:j])
            if len(ans)==0:
                ans=S[i:j]
            elif len(ans)> len(S[i:j]):
                ans=S[i:j]
            currhash[S[i]]-=1
            if currhash[S[i]]==mainhash[S[i]]:
                count-=1
            i+=1
        return ans
    S=input()
    P=input()
    ans=SmallestWindow(S,P)
    if len(ans)==0:
        print(-1)
    else:
        print(ans)

if __name__=='__main__':
    main()
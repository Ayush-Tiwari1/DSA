

def main():
    def maxHeight(h,b,l,n):
        def compare(val):
            return val[1]*val[2]
        def LIS(dim,n):
            lis=[]
            for i in range(n):
                lis.append(dim[i][0])
            ans=lis[0]
            for i in range(1,n):
                maxi=0
                for j in range(0,i):
                    if dim[j][1]>dim[i][1] and  dim[j][2]>dim[i][2]:
                        maxi=max(maxi,lis[j])
                lis[i]+=maxi
                ans=max(ans,lis[i])
            # print(lis)
            return ans
        dim=[]
        for i in range(n):
            arr=[h[i],b[i],l[i]]
            arr.sort()
            dim.append([arr[0],arr[1],arr[2]])
            dim.append([arr[1],arr[0],arr[2]])
            dim.append([arr[2],arr[0],arr[1]])
        dim.sort(key=compare,reverse=True)
        ans=LIS(dim,len(dim))
        return ans
    t=int(input())
    for _ in range(t):
        n=int(input())
        h=list(map(int,input().split()))
        b=list(map(int,input().split()))
        l=list(map(int,input().split()))
        ans=maxHeight(h,b,l,n)
        print(ans)

if __name__=='__main__':
    main()
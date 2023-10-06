# Print Abbreviations

def PrintAbbreviations(string,temp,count,ans):
    if string=="":
        if count>0:
            ans.append(temp+str(count))
        else:
            ans.append(temp)
        return
    # Include
    if count>0:
        PrintAbbreviations(string[1:],temp+str(count)+string[0],0,ans)
    else:
        PrintAbbreviations(string[1:],temp+string[0],0,ans)
    # Exclude
    PrintAbbreviations(string[1:],temp,count+1,ans)


def main():
    string=input()
    ans=[]
    PrintAbbreviations(string,"",0,ans)
    ans.sort()
    for string in ans:
        print(string,end= " ")
    print()




if __name__=='__main__':
    main()
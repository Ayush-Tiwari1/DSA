# Permutations of a String


def Permutations(string,ans):
    if string=="":
        print(ans)
        return
    for i in range(len(string)):
        substr1=string[0:i]
        substr2=string[i+1:]
        Permutations(substr1+substr2,ans+string[i])



def main():
    string=input()
    Permutations(string,"")





if __name__=='__main__':
    main()
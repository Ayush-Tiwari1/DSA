# Print Encodings

dict={
    '1':'a',
    '2':'b',
    '3':'c',
    '4':'d',
    '5':'e',
    '6':'f',
    '7':'g',
    '8':'h',
    '9':'i',
    '10':'j',
    '11':'k',
    '12':'l',
    '13':'m',
    '14':'n',
    '15':'o',
    '16':'p',
    '17':'q',
    '18':'r',
    '19':'s',
    '20':'t',
    '21':'u',
    '22':'v',
    '23':'w',
    '24':'x',
    '25':'y',
    '26':'z'
}

def PrintEncodings(str,temp,ans):
    if str=="":
        ans.append(temp)
        return
    if str[0]=="0":
        return
    PrintEncodings(str[1:],temp+dict[str[0]],ans)
    if len(str)>1:
        val=str[0:2]
        if val in dict:
            PrintEncodings(str[2:],temp+dict[val],ans)
    



def main():
    str=input()
    ans=[]
    PrintEncodings(str,"",ans)
    for word in ans:
        print(word)


if __name__=='__main__':
    main()
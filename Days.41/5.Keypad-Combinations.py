# Keypad Combinations


def KeypadCombinations(indx,digits,dict):
    if indx==len(digits)-1:
        words=[]
        letters=dict[digits[indx]]
        for letter in letters:
            words.append(letter)
        return words
        
    words=KeypadCombinations(indx+1,digits,dict)
    letters=dict[digits[indx]]
    ans=[]
    for letter in letters:
        for word in words:
            ans.append(letter+word)
            
    return ans



def main():
    digits=input()
    dict={
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
    }
    words=KeypadCombinations(0,digits,dict)
    for word in words:
        print(word)




if __name__=='__main__':
    main()
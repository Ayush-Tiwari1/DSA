#Word Ladder 
#BFS
from queue import Queue

def WordLadder(n,startWord,endWord,wlist):
    wordList=set(wlist)
    if endWord not in wordList:
        return 0
    q=Queue()
    q.put(startWord)
    visited=set()
    visited.add(startWord)
    count=0
    while q.empty()==False:
        size=q.qsize()
        count+=1
        for _ in range(size):
            temp=q.get()
            if temp==endWord:
                return count
            for i in range(len(temp)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    newword=temp[:i]+ch+temp[i+1:]
                    if newword in wordList and newword not in visited:
                        visited.add(newword)
                        q.put(newword)
    return 0
    

def main():
    n=int(input())
    wordlist=[]
    for i in range(n):
        wordlist.append(input().strip())
    startWord=input().strip()
    endWord=input().strip()
    ans=WordLadder(n,startWord,endWord,wordlist)
    if ans==0:
        print('Word Not Found')
    else:
        print(ans)


main()
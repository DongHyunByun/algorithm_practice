for t in range(int(input())):
    wordList=(" ".join(input())).split(" ")
    numOfHy=int(input())
    locOfHy=list(map(int,input().split()))
    numOfHyEachLoc=[0 for i in range(len(wordList)+1)]
    for i in locOfHy:
        numOfHyEachLoc[i]+=1
    print(f"#{t+1}",numOfHyEachLoc[0]*"-",end="")
    for i in range(len(wordList)):
        print(wordList[i]+numOfHyEachLoc[i+1]*"-",end="")
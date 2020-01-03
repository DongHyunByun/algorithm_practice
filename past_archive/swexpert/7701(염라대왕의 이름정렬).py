for t in range(int(input())):
    dic={}
    N=int(input())
    for i in range(N):
        word=input()
        size=len(word)
        if (size in dic):
            dic[size].add(word)
        else:
            dic[size]={word}

    
    sortedKey=sorted(dic)
    print(f"#{t+1}")
    for i in sortedKey:
        myList=sorted(list(dic[i]))
        for i in myList:
            print(i)
    
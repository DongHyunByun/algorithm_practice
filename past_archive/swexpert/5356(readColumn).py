for t in range(int(input())):
    maxLen=0
    a=[]
    for x in range(5):
        word=input()
        a.append(word)
        if len(word)>maxLen:
            maxLen=len(word)
    print(f"#{t+1}",end=" ")
    for i in range(maxLen):
        for j in range(5):
            try :
                print(a[j][i],end="")
            except IndexError :
                continue
    print("")
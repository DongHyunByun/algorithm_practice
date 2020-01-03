for t in range(int(input())):
    word=input()
    ispalin=True
    for i in range(int(len(word)/2)):
        if  (word[i]!=word[-(i+1)]  and  word[i]!="?" and word[-(i+1)]!="?") :
            print(f"#{t+1} Not exist")
            ispalin=False
            break
    if ispalin:
        print(f"#{t+1} Exist")


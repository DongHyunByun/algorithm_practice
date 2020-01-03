for t in range(int(input())):
    word=input()
    ispalin=True
    for i in range(int(len(word)/2)):
        if word[i]=="*" or word[len(word)-1-i]=="*":
            break
        elif word[i]!=word[len(word)-1-i]:
            ispalin=False
            print(f"#{t+1} Not exist")
            break
        else:
            continue
    if ispalin:
        print(f"#{t+1} Exist")


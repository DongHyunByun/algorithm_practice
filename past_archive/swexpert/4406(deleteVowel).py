for t in range(int(input())):
    word=input()
    print(f"#{t+1}",end=" ")
    for i in word:
        if i in ["a","e","i","o","u"]:
            continue
        else :
            print(i,end="")
    print("")

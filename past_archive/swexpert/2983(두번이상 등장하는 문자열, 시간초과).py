for t in range(int(input())):
    N=int(input())
    word=input()
    commonWord=""
    toWord=""
    LongestNum=0
    

    for i in word:
        #i추가해도 공통이면
        if commonWord+i in toWord:
            commonWord+=i
            toWord+=i
            continue
        #공통부분끝
        else:
            if LongestNum<len(commonWord):
                print("최장단어는",commonWord)
                LongestNum=len(commonWord)

            if i in toWord:
                commonWord=i
            else:
                commonWord=""
            toWord+=i


    if LongestNum<len(commonWord):
        LongestNum=len(commonWord)
        print("최장단어는",commonWord)

    print(f"#{t+1} {LongestNum}")

for t in range(int(input())):
    L=[]
    for i in range(int(input())):
        L.append(list(map(int,input().split())))
    print(f"#{t+1}")
    for i in range(len(L)):
        for fir in range(len(L)-1,-1,-1):
            print(L[fir][i],end="")
        print(" ",end="")
        for second in range(len(L)-1,-1,-1):
            print(L[len(L)-i-1][second],end="")
        print(" ",end="")
        for third in range(len(L)):
            print(L[third][len(L)-i-1],end="")
        print(" ",end="")
        print("")




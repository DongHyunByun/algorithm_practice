for t in range(10):
    t=int(input())
    myL=[]
    for i in range(100):
        tempL=list(map(int,input().split()))
        myL.append(tempL)
    #가로
    max=0
    for i in range(100):
        if max<sum(myL[i]):
            max=sum(myL[i])

    #세로
    for j in range(100):
        colSum=0
        for row in range(100):
            colSum+=myL[row][j]
        if (max<colSum):
            max=colSum

    #우하대각선
    diaSum=0
    for i in range(100):
        diaSum+=myL[i][i]
    if(max<diaSum):
        max=diaSum

    #우상대각선
    diaSum=0
    for i in range(100):
        diaSum+=myL[99-i][i]
    if(max<diaSum):
        max=diaSum

    print(f"#{t} {max}")
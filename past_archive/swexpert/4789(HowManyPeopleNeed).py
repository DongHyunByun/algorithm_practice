for t in range(int(input())):
    peopleDemandL=list(map(int,input()))
    nowClap=peopleDemandL[0]
    sumOfEmploy=0
    for i in range(1,len(peopleDemandL)):
        if peopleDemandL[i]==0:
            continue
        elif (nowClap>=i) :
            nowClap+=peopleDemandL[i]
        else :
            employ=i-nowClap
            sumOfEmploy+=employ
            nowClap+=employ+peopleDemandL[i]
    print(f"#{t+1} {sumOfEmploy}")
  
for t in range(int(input())):
    L=list(map(int,input().split()))
    totalMinute=(L[0]+L[2])*60+(L[1]+L[3])
    if (totalMinute//60)%12==0:
        a=12
    else :
        a=(totalMinute//60)%12

    print(f"#{t+1} {a} {totalMinute%60}") 
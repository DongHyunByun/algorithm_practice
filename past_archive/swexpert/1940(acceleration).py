for t in range(int(input())):
    sped=0
    d=0
    for n in range(int(input())):
        tem=list(map(int,input().split()))
        if tem[0]==1:
            sped+=tem[1]
        elif tem[0]==2:
            sped-=tem[1]
            if sped<0:
                sped=0
        d+=sped
    print(f"#{t+1} {d}")
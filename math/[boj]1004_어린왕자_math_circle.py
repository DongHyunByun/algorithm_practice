T=int(input())

for t in range(T):
    x1,y1,x2,y2=map(int,input().split())
    N=int(input())
    cnt=0
    for n in range(N):
        cx,cy,r=map(int,input().split())
        srtIn=False
        finIn=False

        # 출발점이 해당원 안에 있는가?
        if (x1 - cx) ** 2 + (y1 - cy) ** 2 < r**2:
            srtIn=True
        # 도착점이 해당원 안에 있는가?
        if (x2 - cx) ** 2 + (y2 - cy) ** 2 < r ** 2:
            finIn=True

        if (srtIn and not finIn) or (not srtIn and finIn):
            cnt+=1
    print(cnt)



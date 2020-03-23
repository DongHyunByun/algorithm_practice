dR=[0,0,-1,1]
dC=[1,-1,0,0]
rever=[1,0,3,2]
N,K=map(int,input().split())
mapColor=[]
for i in range(N):
    mapColor.append(list(map(int,input().split())))
loc=[]
mapHorse=[[[] for j in range(N)] for i in range(N)]
for i in range(K):
    r,c,to=map(int,input().split())
    loc.append([r-1,c-1])
    mapHorse[r-1][c-1].append([i,to-1])
ans=-1
isAns=False

#현재위치(r,c) -> 다음위치(tempR,tempC), 현재층 order
def doWhite(r,c,tempR,tempC,order):
    temp=list(mapHorse[r][c][order:])
    mapHorse[tempR][tempC].extend(temp)
    del mapHorse[r][c][order:]
    # 위치이동 표시
    for hor in temp:
        horseNum = hor[0]
        loc[horseNum][0] = tempR
        loc[horseNum][1] = tempC
def doRed(r,c,tempR,tempC,order):
    temp = list(reversed(list(mapHorse[r][c][order:])))
    mapHorse[tempR][tempC].extend(temp)
    del mapHorse[r][c][order:]
    for hor in temp:
        horseNum = hor[0]
        loc[horseNum][0] = tempR
        loc[horseNum][1] = tempC

#동작시작
for time in range(1,1001):
    #print(time,"번째 시작@@@@@@@@@@@@@")
    #말하나씩 이동
    for i in range(K):
        r=loc[i][0]
        c=loc[i][1]
        # order : 해당말의 층, 방향찾기
        for j in range(len(mapHorse[r][c])):
            if mapHorse[r][c][j][0]==i:
                to=mapHorse[r][c][j][1]
                order=j
                break
        # 이동할 위치 상태확인
        tempR=r+dR[to]
        tempC=c+dC[to]
        #칸안일때
        if 0<=tempR<N and 0<=tempC<N:
            #흰색이면?
            if mapColor[tempR][tempC]==0:
                doWhite(r,c,tempR,tempC,order)
            #빨강이면?
            elif mapColor[tempR][tempC]==1:
                doRed(r,c,tempR,tempC,order)
            #파랑이면?
            else:
                #방향바꿈
                mapHorse[r][c][order][1] = rever[to]
                tempR = r + dR[rever[to]]
                tempC = c + dC[rever[to]]
                if 0<=tempR<N and 0<=tempC<N:
                    if mapColor[tempR][tempC]==0:
                        doWhite(r,c,tempR,tempC,order)
                    elif mapColor[tempR][tempC]==1:
                        doRed(r,c,tempR,tempC,order)
        #칸밖일때?
        else:
            mapHorse[r][c][order][1]=rever[to]
            tempR=r+dR[rever[to]]
            tempC=c+dC[rever[to]]
            #반대편 흰색일때
            if mapColor[tempR][tempC]==0:
                doWhite(r,c,tempR,tempC,order)
            #반대편이 빨간색일때
            elif mapColor[tempR][tempC]==1:
                doRed(r,c,tempR,tempC,order)

        '''
        print(i,"말이 움직인 후 상황")
        for n in range(N):
            print(mapHorse[n])
        '''
        if 0<=tempR<N and 0<=tempC<N and len(mapHorse[tempR][tempC])>=4:
            isAns=True
            break
    if isAns:
        ans=time
        break
    '''
    print(time,"이동 후 상황")
    for n in range(N):
        print(mapHorse[n])
    print(loc)
    '''
print(ans)


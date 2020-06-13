dR=[-1,0,1,0]
dC=[0,1,0,-1]
curve=[0,[2,3,1,0],[1,3,0,2],[3,2,0,1],[2,0,3,1],[2,3,0,1]]

T=int(input())
for t in range(T):
    L=[]
    N=int(input())

    for i in range(N):
        L.append(list(map(int,input().split())))

    # 웜홀작업
    worm = {}
    for i in range(6,11):
        worm[i]=[]
    for i in range(N):
        for j in range(N):
            if 6<=L[i][j]<=10:
                worm[L[i][j]].append((i,j))
    warp={}
    for i in range(6,11):
        if worm[i]:
            warp[worm[i][0]]=worm[i][1]
            warp[worm[i][1]]=worm[i][0]

    ans=0
    for i in range(N):
        for j in range(N):
            if L[i][j]==0:
                for k in range(4):
                    #(i,j)에서 k방향으로 case 시작
                    r=i
                    c=j
                    to=k
                    score=0
                    while(1):
                        #print(r,c,to)
                        tempR=r+dR[to]
                        tempC=c+dC[to]
                        #벽아님
                        if 0<=tempR<N and 0<=tempC<N:
                            #블랙홀이거나 처음위치로오면 종료
                            if L[tempR][tempC]==-1 or [tempR,tempC]==[i,j]:
                                break
                            #블록이면
                            elif 1<=L[tempR][tempC]<=5:
                                score+=1
                                to=curve[L[tempR][tempC]][to]
                                r=tempR
                                c=tempC
                            #빈공간이면
                            elif L[tempR][tempC]==0:
                                r=tempR
                                c=tempC
                            #웜홀
                            else:
                                r,c=warp[(tempR,tempC)]
                        #벽에 부딪힘
                        else:
                            score+=1
                            to=curve[5][to]
                            r=tempR
                            c=tempC
                            continue
                    if score>ans:
                        ans=score
    print("#%d %d"%(t+1,ans))

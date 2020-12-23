dR=[-1,-1,0,1,1,1,0,-1]
dC=[0,1,1,1,0,-1,-1,-1]

N,M,K=map(int,input().split())
ball={}
nowBallNum=M
L=[[[] for j in range(N)] for i in range(N)]

for i in range(M):
    r,c,m,s,d=map(int,input().split())
    ball[i]=[r-1,c-1,m,s,d]
    L[r-1][c-1].append(i)

def move():
    for ballNum in ball:
        r, c, m, s, d = ball[ballNum]

        #원래꺼 삭제
        L[r][c].remove(ballNum)

        #새로운곳에 배치
        tempR=(r+dR[d]*s)%N
        tempC=(c+dC[d]*s)%N
        L[tempR][tempC].append(ballNum)
        ball[ballNum]=[tempR,tempC,m,s,d]

def cheak():
    global nowBallNum
    for i in range(N):
        for j in range(N):
            size=len(L[i][j])
            if size>=2:
                totalMass=0
                totalSpeed=0
                isSame=[] #짝수면0, 홀수면1
                for key in L[i][j]:
                    r,c,m,s,d=ball[key]
                    totalMass+=m
                    totalSpeed+=s
                    if d%2==0:
                        isSame.append(0)
                    else:
                        isSame.append(1)
                    del ball[key]

                L[i][j] = []
                mass=totalMass//5
                speed=totalSpeed//size
                isSameSum=sum(isSame)
                if mass!=0:
                    if isSameSum==0 or isSameSum==size:
                        dir=[0,2,4,6]
                    else:
                        dir=[1,3,5,7]
                    for k in range(4):
                        L[i][j].append(nowBallNum)
                        ball[nowBallNum]=[i,j,mass,speed,dir[k]]
                        nowBallNum+=1

for _ in range(K):
    # print(_,"번째")
    move()
    # for i in L:
    #     print(i)
    # print(ball)
    cheak()
    # for i in L:
    #     print(i)
    # print(ball)

ans=0
for i in range(N):
    for j in range(N):
        for key in L[i][j]:
            ans+=ball[key][2]

print(ans)












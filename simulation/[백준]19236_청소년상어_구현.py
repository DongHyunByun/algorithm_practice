from copy import deepcopy
dR=[-1,-1,0,1,1,1,0,-1]
dC=[0,-1,-1,-1,0,1,1,1]

L=[[[0,0] for j in range(4)] for i in range(4)]

fishD={}
for i in range(1,17):
    fishD[i]=[0,0]

for i in range(4):
    temp=list(map(int,input().split()))
    for j in range(8):
        a=j//2
        b=j%2
        L[i][a][b]=temp[j]
        if b==0:
            fishD[L[i][a][b]]=[i,a]

def fishMove(L,fishD):
    for fish in range(1,17):
        r,c=fishD[fish]
        # 먹혀서 없으면
        if r==-1:
            continue
        else:
            d=L[r][c][1]
            d-=1
            for k in range(8):
                tempD=(d+k)%8
                tempR=r+dR[tempD]
                tempC=c+dC[tempD]

                if 0<=tempR<4 and 0<=tempC<4 and L[tempR][tempC][0]!=-1:
                    newF, newD = L[tempR][tempC]
                    # 비어있을때
                    if newF==0:
                        L[tempR][tempC]=[fish,tempD+1]
                        L[r][c]=[0,0]
                        fishD[fish]=[tempR,tempC]
                        break
                    # 물고기 있을때 위치교환
                    else:
                        L[tempR][tempC]=[fish,tempD+1]
                        L[r][c]=[newF,newD]

                        fishD[fish]=[tempR,tempC]
                        fishD[newF]=[r,c]
                        break

def dfs(L,fD,sR,sC,nowEat):
    global ans
    # 물고기 이동
    fishMove(L,fD)

    d = L[sR][sC][1] - 1
    L[sR][sC] = [0, 0]

    isStop=True
    for k in range(1,4):
        tempR=sR+k*dR[d]
        tempC=sC+k*dC[d]
        if 0<=tempR<4 and 0<=tempC<4 :
            # 비어있지 않으면
            if L[tempR][tempC][0] != 0:

                isStop=False
                copiedL=deepcopy(L)
                copiedD=dict(fD)

                #물고기먹기
                fishNum=copiedL[tempR][tempC][0]
                copiedL[tempR][tempC][0] = -1
                copiedD[fishNum]=[-1,-1]



                dfs(copiedL,copiedD,tempR,tempC,nowEat+fishNum)
        else:
            break


    if isStop==True:
        if ans<nowEat:
            ans=nowEat

# 상어투입
fishNum=L[0][0][0]
L[0][0][0]=-1
fishD[fishNum]=[-1,-1]
ans=0

dfs(L,fishD,0,0,fishNum)
print(ans)



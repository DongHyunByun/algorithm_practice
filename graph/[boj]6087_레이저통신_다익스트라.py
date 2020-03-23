import heapq
import sys
dR=[-1,0,0,1]
dC=[0,-1,1,0]
maxNum=9876543210

#입력
W,H=map(int,input().split())
L=[]
for i in range(H):
    L.append(list(input()))

#시작점찾기
stFin=[]
for i in range(H):
    for j in range(W):
        if L[i][j]=="C":
            stFin.append([i,j])

nodeDist=[[[maxNum for k in range(4)] for j in range(W)] for i in range(H)]
dij=[]
for k in range(4):
    nodeDist[stFin[0][0]][stFin[0][1]][k]=0
    heapq.heappush(dij,[0,stFin[0][0],stFin[0][1],k])
#다익스트라 시작
while(dij):
    nowCost,r,c,to=heapq.heappop(dij)

    if nodeDist[r][c][to]<nowCost:
        continue
    # 도착점인지확인
    if r == stFin[1][0] and c == stFin[1][1]:
        print(nowCost)
        break
    for k in range(4):
        tempR=r+dR[k]
        tempC=c+dC[k]
        #같은방향이면
        if k==to:
            if 0<=tempR<H and 0<=tempC<W and nodeDist[tempR][tempC][k]>nowCost:
                if L[tempR][tempC]=="*":
                    continue
                else:
                    nodeDist[tempR][tempC][k]=nowCost
                    heapq.heappush(dij,[nowCost,tempR,tempC,k])
        #반대방향이면
        elif k==3-to:
            continue
        #꺾이면
        else:
            if 0<=tempR<H and 0<=tempC<W and nodeDist[tempR][tempC][k]>nowCost+1:
                if L[tempR][tempC]=="*":
                    continue
                else:
                    nodeDist[tempR][tempC][k]=nowCost+1
                    heapq.heappush(dij,[nowCost+1,tempR,tempC,k])



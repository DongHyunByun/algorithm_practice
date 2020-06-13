import heapq
import sys

N,M=map(int,input().split())
dR=[0,0,-1,1]
dC=[1,-1,0,0]
INF=9876543210
L=[]
fR,fC,sR,sC=0,0,0,0
for i in range(N):
    L.append(list(input()))

#시작점, 끝점, 쓰레기주변 확인
for i in range(N):
    for j in range(M):
        if L[i][j]=="F":
            fR,fC=i,j
        elif L[i][j]=="S":
            sR,sC=i,j
        elif L[i][j]=="g":
            for k in range(4):
                tempR=i+dR[k]
                tempC=j+dC[k]
                if 0<=tempR<N and 0<=tempC<M and L[tempR][tempC]==".":
                    L[tempR][tempC]="gNear"

nodeDist=[[[INF,INF] for j in range(M)] for i in range(N)]
nodeDist[sR][sC]=[0,0]
dij=[[0,0,sR,sC]]

while(dij):
    point,near,r,c=heapq.heappop(dij)
    if nodeDist[r][c]<[point,near]:
        continue

    for k in range(4):
        tempR=r+dR[k]
        tempC=c+dC[k]
        if 0<=tempR<N and 0<=tempC<M:
            # 쓰레기
            if L[tempR][tempC]=="g":
                if [point+1,near]<nodeDist[tempR][tempC]:
                    nodeDist[tempR][tempC]=[point+1,near]
                    heapq.heappush(dij,[point+1,near,tempR,tempC])
            # 쓰레기 주변
            elif L[tempR][tempC]=="gNear":
                if [point,near+1]<nodeDist[tempR][tempC]:
                    nodeDist[tempR][tempC]=[point,near+1]
                    heapq.heappush(dij,[point,near+1,tempR,tempC])
            # 도착지
            elif L[tempR][tempC]=="F":
                print(point,near)
                sys.exit()
            # 빈공간
            else:
                if [point,near]<nodeDist[tempR][tempC]:
                    nodeDist[tempR][tempC]=[point,near]
                    heapq.heappush(dij,[point,near,tempR,tempC])







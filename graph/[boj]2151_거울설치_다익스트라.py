import heapq

dR=[0,1,-1,0]
dC=[1,0,0,-1]

N=int(input())
L=[]
for i in range(N):
    L.append(list(input()))

isFind=False
for i in range(N):
    for j in range(N):
        if L[i][j]=="#":
            startR=i
            startC=j
            isFind=True
            break
    if isFind:
        break

maxNum=9876543210
nodeDist=[[[maxNum,maxNum,maxNum,maxNum] for j in range(N)] for i in range(N)]

def dijstra():
    dij=[[0,startR,startC,4]]
    for k in range(4):
        nodeDist[startR][startC][k]=0
    heapq.heapify(dij)
    while(dij):
        nowCost,r,c,d=heapq.heappop(dij)


        # 종료 #이면?
        if [r,c]!=[startR,startC] and L[r][c]=="#":
            print(nowCost)
            break

        # 시작 #이면?
        if L[r][c]=="#":
            for k in range(4):
                tempR=r+dR[k]
                tempC=c+dC[k]
                if 0<=tempR<N and 0<=tempC<N and L[tempR][tempC]!="*":
                    nodeDist[tempR][tempC][k]=0
                    dij.append([0,tempR,tempC,k])
        # . 이면?
        elif L[r][c]==".":
            # 이미방문되었으면 종료
            if nodeDist[r][c][d]<nowCost:
                continue
            tempR=r+dR[d]
            tempC=c+dC[d]
            if 0<=tempR<N and 0<=tempC<N and L[tempR][tempC]!="*" and nowCost<nodeDist[tempR][tempC][d]:
                nodeDist[tempR][tempC][d]=nowCost
                heapq.heappush(dij,[nowCost,tempR,tempC,d])
        # !이면?
        else:
            if nodeDist[r][c][d]<nowCost:
                continue
            for k in range(4):
                if k+d==3:
                    continue
                # 거울설치 안하면?
                elif k==d:
                    tempR=r+dR[k]
                    tempC=c+dC[k]
                    if 0<=tempR<N and 0<=tempC<N and L[tempR][tempC]!="*" and nowCost<nodeDist[tempR][tempC][d]:
                        nodeDist[tempR][tempC][d]=nowCost
                        heapq.heappush(dij,[nodeDist[tempR][tempC][d],tempR,tempC,d])
                # 거울설치?
                else:
                    tempR=r+dR[k]
                    tempC=c+dC[k]
                    if 0<=tempR<N and 0<=tempC<N and L[tempR][tempC]!="*" and nowCost+1<nodeDist[tempR][tempC][k]:
                        nodeDist[tempR][tempC][k]=nowCost+1
                        heapq.heappush(dij,[nodeDist[tempR][tempC][k],tempR,tempC,k])




dijstra()
'''
for i in range(N):
    print(nodeDist[i])
'''

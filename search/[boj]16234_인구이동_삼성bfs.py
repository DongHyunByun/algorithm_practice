from collections import deque

N,L,R=map(int,input().split())
myMap=[]
for i in range(N):
    myMap.append(list(map(int,input().split())))

dR=[0,0,-1,1]
dC=[1,-1,0,0]

ans=0
while(1):
    isMoved=False
    isGroupedL=[[0 for j in range(N)] for i in range(N)]
    # 인접국가 국경열기
    for i in range(N):
        for j in range(N):
            if isGroupedL[i][j]:
                continue
            # group x 시작
            else:
                groupSum=myMap[i][j] # 현재그룹 합
                nowGroup = [[i, j]] # 현재그룹 지역
                isGroupedL[i][j]=1 # 전체방문?
                dq=deque([[i,j]])
                while(dq):
                    temp=dq.popleft()
                    r=temp[0]
                    c=temp[1]
                    for k in range(4):
                        tempR=r+dR[k]
                        tempC=c+dC[k]
                        if 0<=tempR<N and 0<=tempC<N and isGroupedL[tempR][tempC]==0 and L<=abs(myMap[r][c]-myMap[tempR][tempC])<=R:
                            groupSum+=myMap[tempR][tempC]
                            nowGroup.append([tempR,tempC])
                            isGroupedL[tempR][tempC]=1
                            dq.append([tempR,tempC])
                #그룹이 있는경우
                size=len(nowGroup)
                if size!=1:
                    isMoved=True
                    inputNum=groupSum//size
                    for r,c in nowGroup:
                        myMap[r][c]=inputNum
    if isMoved:
        ans+=1
    else:
        break
print(ans)

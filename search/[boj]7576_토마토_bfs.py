from collections import deque
import sys
# 입력받기
N,M=map(int,input().split())
L=[]
for i in range(M):
    L.append(list(map(int,input().split())))

# 시작 q구성
dq=deque([])
for i in range(M):
    for j in range(N):
        if L[i][j]==1:
            dq.append([i,j])
# bfs
dR=[0,0,-1,1]
dC=[1,-1,0,0]

lastDay=0
while(dq):
    temp=dq.popleft()
    r=temp[0]
    c=temp[1]
    for k in range(4):
        tempR=r+dR[k]
        tempC=c+dC[k]
        if 0<=tempR<M and 0<=tempC<N and L[tempR][tempC]==0:
            L[tempR][tempC]=L[r][c]+1
            dq.append([tempR,tempC])


# 답찾기
def sol(d):
    maxNum=1
    for i in range(M):
        for j in range(N):
            if L[i][j]==0:
                print(-1)
                return
            else:
                maxNum=max(maxNum,L[i][j])
    print(maxNum-1)

sol(lastDay)
from collections import deque
import sys

#입력받기
dR=[0,0,-1,1]
dC=[1,-1,0,0]
M,N=map(int,input().split())
L=[]
fR=-1
for i in range(M):
    temp=list(input())
    L.append(temp)

# 초기 훈,불 찾기
hoon=deque([])
fire=deque([])
for i in range(M):
    for j in range(N):
        if L[i][j]=="F":
            fire.append([i,j])
        elif L[i][j]=="J":
            jR, jC = i, j
            hoon.append([i,j])
visited=[[-1 for j in range(N)] for i in range(M)]
visited[jR][jC]=0


def fireSpread():
    global isImpossible
    size=len(fire)
    if size!=0:

        isImpossible=False
    for _ in range(size):
        r,c=fire.popleft()
        for k in range(4):
            tempR=r+dR[k]
            tempC=c+dC[k]
            if 0<=tempR<M and 0<=tempC<N and L[tempR][tempC] not in ["#","F"]:
                L[tempR][tempC]="F"
                fire.append([tempR,tempC])

def moveHoon():
    global isImpossible
    size=len(hoon)
    if size!=0:
        isImpossible=False
    for _ in range(size):
        r,c=hoon.popleft()
        for k in range(4):
            tempR=r+dR[k]
            tempC=c+dC[k]
            if 0<=tempR<M and 0<=tempC<N:
                if L[tempR][tempC]=="." and visited[tempR][tempC]==-1:
                    visited[tempR][tempC]=visited[r][c]+1
                    hoon.append([tempR,tempC])
            #탈출
            else:
                print(visited[r][c]+1)
                sys.exit()

while(1):
    isImpossible=True
    fireSpread()
    moveHoon()
    if isImpossible:
        print("IMPOSSIBLE")
        sys.exit()

from collections import deque
import sys

dR=[0,0,-1,1]
dC=[1,-1,0,0]

R,C=map(int,input().split())
L=[]
bird=[]
for i in range(R):
    temp=list(input())
    if "L" in temp:
        bird.extend([i,temp.index("L")])
    L.append(temp)
r1,c1,r2,c2=bird

#백조 도달가능?
def isPossible(q):
    global swanQ
    nextSwanQ=[]
    while(q):
        r,c=q.popleft()
        for k in range(4):
            tempR=r+dR[k]
            tempC=c+dC[k]
            if 0<=tempR<R and 0<=tempC<C and swanVisited[tempR][tempC]==-1:
                if L[tempR][tempC]==".":
                    q.append([tempR,tempC])
                    swanVisited[tempR][tempC]=1
                elif L[tempR][tempC]=="X":
                    nextSwanQ.append([tempR,tempC])
                    swanVisited[tempR][tempC]=1
                else:
                    return True
    swanQ=deque(nextSwanQ)
    return False

#얼음 녹기
def melt(q):
    global meltQ
    nextMeltQ=[]
    #녹이기
    for r,c in q:
        L[r][c]="."
    #다음 녹일거 찾기
    while(q):
        r,c=q.popleft()
        for k in range(4):
            tempR=r+dR[k]
            tempC=c+dC[k]
            if 0<=tempR<R and 0<=tempC<C and meltVisited[tempR][tempC]==-1:
                if L[tempR][tempC]=="X":
                    meltVisited[tempR][tempC]=1
                    nextMeltQ.append([tempR,tempC])
                else:
                    meltVisited[tempR][tempC]=1
                    q.append([tempR,tempC])
    meltQ=deque(nextMeltQ)

day=0
#백조변수
swanQ=deque([[r1,c1]])
swanVisited=[[-1 for j in range(C)] for i in range(R)]
swanVisited[r1][c1]=1
#빙하녹이기 변수
meltQ=deque([])
meltVisited=[[-1 for j in range(C)] for i in range(R)]
for i in range(R): #초기화
    for j in range(C):
        if L[i][j]!="X" and meltVisited[i][j]==-1:
            meltVisited[i][j]=1
            q=deque([[i,j]])
            while(q):
                r,c=q.popleft()
                for k in range(4):
                    tempR=r+dR[k]
                    tempC=c+dC[k]
                    if 0<=tempR<R and 0<=tempC<C and meltVisited[tempR][tempC]==-1:
                        if L[tempR][tempC]=="X":
                            meltQ.append([tempR,tempC])
                            meltVisited[tempR][tempC]=1
                        else:
                            q.append([tempR, tempC])
                            meltVisited[tempR][tempC] = 1


while(1):
    '''
    for i in L:
        print(i)
    print()
    '''

    if isPossible(swanQ):
        print(day)
        break
    else:
        #물녹기시작
        melt(meltQ)
        day+=1







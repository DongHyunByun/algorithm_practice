from collections import deque
dR=[0,0,-1,1]
dC=[1,-1,0,0]

N,M=map(int,input().split())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))

def flow():
    q=deque([[0,0]])
    visited=[[0 for j in range(M)] for i in range(N)]
    visited[0][0]=2
    while(q):
        r,c=q.popleft()
        for k in range(4):
            tempR=r+dR[k]
            tempC=c+dC[k]
            if 0<=tempR<N and 0<=tempC<M and visited[tempR][tempC]!=2 and L[tempR][tempC]!=1 :
                visited[tempR][tempC]=2
                q.append([tempR,tempC])

    for i in range(N):
        for j in range(M):
            if visited[i][j]==2:
                L[i][j]=2

def isFin():
    for i in range(N):
        for j in range(M):
            if L[i][j]!=2:
                return False
    return True

def countC():
    c=0
    for i in range(N):
        for j in range(M):
            if L[i][j] == 1:
                c += 1
    return c

def melt():
    m=[[0 for j in range(M)] for i in range(N)]

    for i in range(1,N-1):
        for j in range(1,M-1):
            if L[i][j]==1:
                for k in range(4):
                    tempR=i+dR[k]
                    tempC=j+dC[k]
                    if L[tempR][tempC]==2:
                        m[i][j]=1
                        break

    for i in range(N):
        for j in range(M):
            if m[i][j]==1:
                L[i][j]=2

t=0
preC=countC()
while(1):
    # 공기순환
    flow()

    # 종료조건이면?
    if isFin():
        print(t)
        print(preC)
        break

    #시간경과, 이전개수 세기
    t+=1
    preC = countC()

    #치즈 녹이기
    melt()

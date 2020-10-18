from collections import deque

dR=[0,0,-1,1]
dC=[1,-1,0,0]
N,M=map(int,input().split())

L=[]
for i in range(N):
    L.append(list(map(int,input().split())))

def isFin():
    for i in range(N):
        for j in range(M):
            if L[i][j]==1:
                return False
    return True

def flowAir():
    visited=[[0 for j in range(M)] for i in range(N)]
    q = deque([[0, 0]])
    L[0][0] = 2
    while (q):
        r,c=q.popleft()
        for k in range(4):
            tempR=r+dR[k]
            tempC=c+dC[k]
            if 0<=tempR<N and 0<=tempC<M and L[tempR][tempC]!=1 and visited[tempR][tempC]==0:
                L[tempR][tempC]=2
                visited[tempR][tempC]=1
                q.append([tempR,tempC])

ans=0
while(1):
    '''
    print(ans)
    for i in L:
        print(i)
    '''

    #다제거 되었는지 확
    if isFin():
        break

    #공기순환
    flowAir()

    #제거할 치즈 확인
    removeL=[] #제거할 위치 저장
    for i in range(N):
        for j in range(M):
            #네면 확인
            expose=0
            for k in range(4):
                tempR=i+dR[k]
                tempC=j+dC[k]
                if 0<=tempR<N and 0<=tempC<M and L[tempR][tempC]==2:
                    expose+=1
            if expose>=2:
                removeL.append([i,j])

    #치즈 제거
    for r,c in removeL:
        L[r][c]=2

    ans+=1

print(ans)
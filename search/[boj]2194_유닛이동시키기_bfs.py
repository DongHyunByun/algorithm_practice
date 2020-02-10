from collections import deque
dR=[0,-1,0,1]
dC=[-1,0,1,0]

N,M,A,B,K=map(int,input().split())
L=[[-1 for j in range(M)] for i in range(N)]
for i in range(K):
    x,y=map(int,input().split())
    x-=1
    y-=1
    L[x][y]="*"
a,b=map(int,input().split())
a-=1
b-=1
toR,toC=map(int,input().split())
toR-=1
toC-=1

ans=-1
# 안간곳은 -1, 장애물은 *, 숫자는 최단거리
q=deque([[a,b]])
L[a][b]=0
while(q):
    temp=q.popleft()
    r=temp[0]
    c=temp[1]
    if r==toR and c==toC:
        ans=L[r][c]
        break

    for k in range(4):
        tempR = r + dR[k]
        tempC = c + dC[k]
        if k<2:
            if 0<=tempR<N and 0<=tempC<M and L[tempR][tempC]==-1:
                #첫행 or 첫열 검사
                canGo=True
                for j in range(B):
                    if L[tempR][tempC+j]=="*":
                        canGo=False
                        break
                for i in range(A):
                    if L[tempR+i][tempC]=="*":
                        canGo=False
                        break
                if canGo:
                    L[tempR][tempC]=L[r][c]+1
                    q.append([tempR,tempC])
        else:
            endC = tempC + B - 1
            endR = tempR + A - 1
            if endC<M and endR<N and L[tempR][tempC]==-1 :
                canGo=True
                for j in range(B):
                    if L[endR][tempC+j]=="*":
                        canGo=False
                        break
                for i in range(A):
                    if L[tempR+i][endC]=="*":
                        canGo=False
                        break
                if canGo:
                    L[tempR][tempC]=L[r][c]+1
                    q.append([tempR,tempC])
print(ans)
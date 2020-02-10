from itertools import combinations
from copy import deepcopy
from collections import deque

N,M=map(int,input().split())

L=[]
for i in range(N):
    L.append(list(map(int,input().split())))

numL=[i for i in range(N*M)]
combi=list(combinations(numL,3))
dR=[0,0,-1,1]
dC=[1,-1,0,0]

ans=0

for a,b,c in combi:
    r1=a//M
    c1=a%M
    r2=b//M
    c2=b%M
    r3=c//M
    c3=c%M
    if (L[r1][c1]==0 and L[r2][c2]==0 and L[r3][c3]==0) :
        coL=deepcopy(L)
        visitedL=[[0 for j in range(M)] for i in range(N)]

        coL[r1][c1]=1
        coL[r2][c2]=1
        coL[r3][c3]=1

        for iniR in range(N):
            for iniC in range(M):
                # 큐시작
                if (coL[iniR][iniC]==2 and visitedL[iniR][iniC]==0) :
                    dq=deque([[iniR,iniC]])
                    while(dq):
                        R,C=dq.popleft();
                        for k in range(4):
                            tempR=R+dR[k]
                            tempC=C+dC[k]
                            if (0<=tempR<N and 0<=tempC<M and coL[tempR][tempC]!=1 and visitedL[tempR][tempC]==0 ):
                                dq.append([tempR,tempC])
                                coL[tempR][tempC]=2
                                visitedL[tempR][tempC]=1
        cnt=0
        for i in range(N):
            for j in range(M):
                if coL[i][j]==0:
                    cnt+=1
        if cnt>ans:
            ans=cnt

print(ans)


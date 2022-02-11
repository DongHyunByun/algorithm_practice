from collections import deque

N,M=map(int,input().split())
dR=[0,0,-1,1]
dC=[1,-1,0,0]

L=[]
for i in range(N):
    L.append(list(map(int,input().split())))

def grouping(normal,sr,sc):
    # 개수, 무지개블록의 수 반환
    q=deque([(sr,sc)])
    while(q):
        r,c=q.popleft()
        for k in range(4):
            tempR=r+dR[k]
            tempC=c+dC[k]
            if 0<=tempR<N and 0<=tempC<N and visited[tempR][tempC]==-1 and L[tempR][tempC]

while(1):
    visited=[[-1 for j in range(N)] for i in range(N)]
    group={}
    for i in range(N):
        for j in range(N):
            if visited[i][j]==-1 and L[i][j]>0:
                normal=L[i][j]
                sr=i
                sc=j
                grouping(normal,sr,sc)





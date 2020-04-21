from collections import deque
dR=[-1,-1,-1,0,0,0,1,1,1]
dC=[-1,0,1,-1,0,1,-1,0,1]

N,M=map(int,input().split())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))
visited=[[0 for j in range(M)] for i in range(N)]

cnt=0
for i in range(N):
    for j in range(M):
        if visited[i][j]==0:
            height=L[i][j]
            visited[i][j]=1
            q=deque([[i,j]])
            isTop=True
            while(q):
                r,c=q.popleft()
                for k in range(9):
                    tempR=r+dR[k]
                    tempC=c+dC[k]
                    if 0<=tempR<N and 0<=tempC<M:
                        if L[tempR][tempC]==height and visited[tempR][tempC]==0:
                            q.append([tempR,tempC])
                            visited[tempR][tempC]=1
                        elif L[tempR][tempC]>height:
                            isTop=False

            if isTop:
                cnt+=1

print(cnt)
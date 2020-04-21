from collections import deque

dR=[0,0,-1,1]
dC=[1,-1,0,0]
N,M=map(int,input().split())
L=[]
for i in range(M):
    L.append(list(input()))
visited=[[0 for j in range(N)] for i in range(M)]
score=[0,0]
for i in range(M):
    for j in range(N):
        if visited[i][j]==0:
            q=deque([[i,j]])
            visited[i][j]=1
            cnt=1
            pia=L[i][j]
            while(q):
                r,c=q.popleft()
                for k in range(4):
                    tempR=r+dR[k]
                    tempC=c+dC[k]
                    if 0<=tempR<M and 0<=tempC<N and visited[tempR][tempC]==0 and L[tempR][tempC]==pia:
                        visited[tempR][tempC]=1
                        cnt+=1
                        q.append([tempR,tempC])

            if pia=="W":
                score[0]+=cnt**2
            else:
                score[1]+=cnt**2

print(*score)


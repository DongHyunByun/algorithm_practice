from collections import deque

dR=[0,0,-1,1]
dC=[1,-1,0,0]

N,M,K=map(int,input().split())

L=[[0 for j in range(M)] for i in range(N)]
visited=[[0 for j in range(M)] for i in range(N)]

for i in range(K):
    a,b=map(int,input().split())
    L[a-1][b-1]=1

ans=0
for i in range(N):
    for j in range(M):
        if L[i][j]==1 and visited[i][j]==0:
            cnt=1
            visited[i][j]=1
            q=deque([[i,j]])
            while(q):
                r,c=q.popleft()
                for k in range(4):
                    tempR=r+dR[k]
                    tempC=c+dC[k]
                    if 0<=tempR<N and 0<=tempC<M and visited[tempR][tempC]==0 and L[tempR][tempC]==1:
                        visited[tempR][tempC]=1
                        q.append([tempR,tempC])
                        cnt+=1
            if ans<cnt:
                ans=cnt
print(ans)
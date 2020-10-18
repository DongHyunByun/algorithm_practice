from collections import deque

dR=(0,0,-1,1)
dC=(1,-1,0,0)

N,M,K=map(int,input().split())
L=[]
for i in range(N):
   L.append(input())

visited=[[[-1 for k in range(K+1)] for j in range(M)] for i in range(N)]
visited[0][0][0]=1
q=deque([[0,0,0]])
ans=-1

while(q):
    r,c,k=q.popleft()

    if r==N-1 and c==M-1:
        ans=visited[r][c][k]
        break
    for i in range(4):
        tempR=r+dR[i]
        tempC=c+dC[i]
        if 0<=tempR<N and 0<=tempC<M and visited[tempR][tempC][k]==-1:
            # 뚫려있으면
            if L[tempR][tempC]=="0":
                visited[tempR][tempC][k]=visited[r][c][k]+1
                q.append([tempR,tempC,k])
            # 벽이면
            else:
                if k<K and visited[tempR][tempC][k+1]==-1:
                    visited[tempR][tempC][k+1]=visited[r][c][k]+1
                    q.append([tempR,tempC,k+1])


print(ans)







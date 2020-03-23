from collections import deque
dR=[0,0,-1,1,0,0]
dC=[1,-1,0,0,0,0]
dBox=[0,0,0,0,1,-1]

M,N,H=map(int,input().split())
L=[]
for i in range(H):
    temp=[]
    for j in range(N):
        temp.append(list(map(int,input().split())))
    L.append(temp)

#토마토 모두다 익었는지 확인
def cheak():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                #안익은곳에 방문안했으면
                if L[i][j][k]==0 and visited[i][j][k]==-1:
                    return False
    return True

#익은 토마토찾기
visited=[[[-1 for j in range(M)] for i in range(N)] for box in range(H)]
q=deque([])
for i in range(H):
    for j in range(N):
        for k in range(M):
            if L[i][j][k]==1:
                visited[i][j][k]=0
                q.append([i,j,k])

ans=0
#익히기 시작
while(q):
    box,r,c=q.popleft()
    ans=visited[box][r][c]
    for k in range(6):
        tempBox=box+dBox[k]
        tempR=r+dR[k]
        tempC=c+dC[k]
        if 0<=tempBox<H and 0<=tempR<N and 0<=tempC<M and visited[tempBox][tempR][tempC]==-1 and L[tempBox][tempR][tempC]==0:
            visited[tempBox][tempR][tempC]=visited[box][r][c]+1
            q.append([tempBox,tempR,tempC])

if cheak():
    print(ans)
else:
    print(-1)

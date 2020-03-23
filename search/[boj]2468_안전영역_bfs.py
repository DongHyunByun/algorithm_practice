from collections import deque
dR=[0,0,-1,1]
dC=[1,-1,0,0]
N=int(input())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))

def BFS(rain):
    visited=[[-1 for j in range(N)] for i in range(N)]
    cnt=0
    for i in range(N):
        for j in range(N):
            if L[i][j]>rain and visited[i][j]==-1:
                cnt+=1
                visited[i][j]=cnt
                q=deque([[i,j]])
                while(q):
                    r,c=q.popleft()
                    for k in range(4):
                        tempR=r+dR[k]
                        tempC=c+dC[k]
                        if 0<=tempR<N and 0<=tempC<N and visited[tempR][tempC]==-1 and L[tempR][tempC]>rain:
                            visited[tempR][tempC]=cnt
                            q.append([tempR,tempC])
    return cnt

ans=0
for r in range(0,102):
    num=BFS(r)
    if num==0:
        break
    elif num>ans:
        ans=num
print(ans)
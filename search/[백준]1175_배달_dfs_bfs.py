INF=9876543210
from collections import deque
dR=(-1,0,1,0)
dC=(0,-1,0,1)
N,M=map(int,input().split())
L=[]
for i in range(N):
    L.append(list(input()))


def bfs(case,q,visited):
    while (q):
        r, c, to = q.popleft()
        if L[r][c] == "C":
            case.append([visited[r][c][to],r,c,to])
        for k in range(4):
            if k==to:
                continue
            tempR = r + dR[k]
            tempC = c + dC[k]
            if 0 <= tempR < N and 0 <= tempC < M and L[tempR][tempC] != "#" and visited[tempR][tempC][k] == 0:
                visited[tempR][tempC][k] = visited[r][c][to] + 1
                q.append([tempR, tempC, k])

def dfs(dist,startR,startC,to,cnt):
    global ans

    if ans<=dist:
        return
    #print(dist, startR, startC, to, cnt)
    #두개다 찾았으면
    if cnt==2:
        if dist<ans:
            ans=dist
        return

    visited = [[[0, 0, 0, 0] for j in range(M)] for i in range(N)]
    visited[startR][startC][to] = dist
    q = deque([[startR, startC, to]])
    case=[]
    bfs(case,q,visited)

    for newDist,newR,newC,newTo in case:
        L[newR][newC]="."
        dfs(visited[newR][newC][newTo],newR,newC,newTo,cnt+1)
        L[newR][newC]="C"


# 시작점 찾기
for i in range(N):
    for j in range(M):
        if L[i][j]=="S":
            sR,sC=i,j
            break
L[sR][sC]="."
ans=INF
for k in range(4):
    dfs(0,sR,sC,k,0)

if ans==INF:
    print(-1)
else:
    print(ans)


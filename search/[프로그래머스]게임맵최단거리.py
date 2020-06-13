from collections import deque
dR=[0,0,-1,1]
dC=[1,-1,0,0]

def solution(maps):
    N=len(maps)
    M=len(maps[0])

    visited=[[-1 for j in range(M)] for i in range(N)]
    visited[0][0]=1
    q=deque([[0,0]])
    ans=-1
    while(q):
        r,c=q.popleft()
        if r==N-1 and c==M-1:
            ans=visited[r][c]
            break
        for k in range(4):
            tempR=r+dR[k]
            tempC=c+dC[k]
            if 0<=tempR<N and 0<=tempC<M and visited[tempR][tempC]==-1 and maps[tempR][tempC]==1:
                visited[tempR][tempC]=visited[r][c]+1
                q.append([tempR,tempC])

    return ans
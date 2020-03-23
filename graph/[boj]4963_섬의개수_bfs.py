from collections import deque
dR=[0,0,-1,1,-1,-1,1,1]
dC=[-1,1,0,0,-1,1,-1,1]

while(1):
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    L=[]
    for i in range(h):
        L.append(list(map(int,input().split())))
    visited=[[-1 for j in range(w)] for i in range(h)]
    cnt=0
    for i in range(h):
        for j in range(w):
            if L[i][j]==1 and visited[i][j]==-1:
                cnt+=1
                visited[i][j]=cnt
                q=deque([[i,j]])
                while(q):
                    r,c=q.popleft()
                    for k in range(8):
                        tempR=r+dR[k]
                        tempC=c+dC[k]
                        if 0<=tempR<h and 0<=tempC<w and L[tempR][tempC]==1 and visited[tempR][tempC]==-1:
                            visited[tempR][tempC]=cnt
                            q.append([tempR,tempC])
    print(cnt)
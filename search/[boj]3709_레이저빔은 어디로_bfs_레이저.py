from collections import deque

T=int(input())
dR=[-1,0,1,0]
dC=[0,1,0,-1]

for t in range(T):
    n,r=map(int,input().split())
    L=[[0 for j in range(n+2)] for i in range(n+2)]
    visited=[[[0,0,0,0] for j in range(n+2)] for i in range(n+2)]
    for i in range(r):
        r,c=map(int,input().split())
        L[r][c]=1
    lazerR,lazerC=map(int,input().split())

    if lazerR==0:
        direct=2
    elif lazerR==n+1:
        direct=0
    elif lazerC==0:
        direct=1
    else:
        direct=3

    q=deque([[lazerR,lazerC,direct]])
    visited[lazerR][lazerC][direct]=1
    while(q):
        r,c,d=q.popleft()
        tempR=r+dR[d]
        tempC=c+dC[d]
        if 1<=tempR<=n and 1<=tempC<=n:
            if L[tempR][tempC]==0:
                if visited[tempR][tempC][d]==1:
                    print(0,0)
                    break
                else:
                    visited[tempR][tempC][d]=1
                    q.append([tempR,tempC,d])
            # 우향우
            else:
                d=(d+1)%4
                if visited[tempR][tempC][d]==1:
                    print(0,0)
                    break
                else:
                    visited[tempR][tempC][d]=1
                    q.append([tempR,tempC,d])
        else:
            print(tempR,tempC)
            break






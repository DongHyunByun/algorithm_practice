from collections import deque
dR=[-2,-1,1,2,2,1,-1,-2]
dC=[1,2,2,1,-1,-2,-2,-1]
T=int(input())
for t in range(T):
    I=int(input())
    sR,sC=map(int,input().split())
    fR,fC=map(int,input().split())
    L=[[-1 for j in range(I)] for i in range(I)]
    L[sR][sC]=0
    q=deque([[sR,sC]])
    while(q):
        r,c=q.popleft()
        if r==fR and c==fC:
            print(L[r][c])
            break
        for k in range(8):
            tempR=r+dR[k]
            tempC=c+dC[k]
            if 0<=tempR<I and 0<=tempC<I and L[tempR][tempC]==-1:
                L[tempR][tempC]=L[r][c]+1
                q.append([tempR,tempC])




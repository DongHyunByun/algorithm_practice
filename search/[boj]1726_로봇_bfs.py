from collections import deque

dR=[0,1,0,-1]
dC=[1,0,-1,0]

if __name__=='__main__':
    M,N=map(int,input().split())
    L=[]
    for i in range(M):
        L.append(list(map(int,input().split())))
    stL=list(map(int,input().split()))
    for i in range(3):
        stL[i]-=1
    if stL[2]==1:
        stL[2]=2
    elif stL[2]==2:
        stL[2]=1

    endL=list(map(int,input().split()))
    for i in range(3):
        endL[i]-=1
    if endL[2]==1:
        endL[2]=2
    elif endL[2]==2:
        endL[2]=1

    bfs=[[[-1,-1,-1,-1] for j in range(N)] for i in range(M)]
    bfs[stL[0]][stL[1]][stL[2]]=0
    q=deque([[stL[0],stL[1],stL[2]]])
    ans=0
    while(q):
        '''
        for i in range(M):
            print(bfs[i])
        print()
        '''

        r,c,turn=q.popleft()
        if [r,c,turn]==endL:
            ans=bfs[r][c][turn]
            break
        #3번까지 직진한 후 q넣어
        for jump in range(1,4):
            tempR=r+dR[turn]*jump
            tempC=c+dC[turn]*jump
            if 0 <= tempR < M and 0 <= tempC < N and L[tempR][tempC] != 1 :
                if bfs[tempR][tempC][turn] == -1:
                    bfs[tempR][tempC][turn]=bfs[r][c][turn]+1
                    q.append([tempR,tempC,turn])
            else:
                break
        #3번 회전한 후 q넣어
        for k in [1,-1]:
            tempTurn=(turn+k)%4
            if bfs[r][c][tempTurn]==-1:
                bfs[r][c][tempTurn]=bfs[r][c][turn]+1
                q.append([r,c,tempTurn])

    print(ans)
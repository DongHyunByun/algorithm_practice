from collections import deque
dR=[0,-1,0,1,0]
dC=[0,0,1,0,-1]

def addBc(sR,sC,l,p,a):
    visited=[[-1 for j in range(10)] for i in range(10)]
    visited[sR][sC]=0
    L[sR][sC].append([p,a])

    q=deque([[sR,sC]])
    while(q):
        r,c=q.popleft()
        if visited[r][c]==l:
            return
        for k in range(1,5):
            tempR=r+dR[k]
            tempC=c+dC[k]
            if 0<=tempR<10 and 0<=tempC<10 and visited[tempR][tempC]==-1:
                visited[tempR][tempC]=visited[r][c]+1
                L[tempR][tempC].append([p,a])
                q.append([tempR,tempC])

T=int(input())
for t in range(T):
    M,bc=map(int,input().split())
    L=[[[[0,-1],[0,-1]] for j in range(10)] for i in range(10)]
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    for a in range(bc):
        x,y,l,p=map(int,input().split())
        r=y-1
        c=x-1
        addBc(r,c,l,p,a) #맵만들기

    # 내림차순정렬
    for i in range(10):
        for j in range(10):
            L[i][j].sort(reverse=True)
    '''
    # 맵 확인
    for i in L:
        print(i)
    '''

    locA=[0,0]
    locB=[9,9]
    ans=L[0][0][0][0]+L[9][9][0][0]

    for m in range(M):
        # 이동
        locA[0]+=dR[A[m]]
        locA[1]+=dC[A[m]]
        locB[0]+=dR[B[m]]
        locB[1]+=dC[B[m]]
        # 충전
        #겹치면
        if L[locA[0]][locA[1]][0][1]==L[locB[0]][locB[1]][0][1]:
            ans += L[locA[0]][locA[1]][0][0] + max(L[locB[0]][locB[1]][1][0],L[locA[0]][locA[1]][1][0])
        #안겹치면 각각 가장큰거
        else:
            ans += L[locA[0]][locA[1]][0][0] + L[locB[0]][locB[1]][0][0]
    print("#%d %d"%(t+1,ans))


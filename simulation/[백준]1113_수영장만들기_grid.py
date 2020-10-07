from collections import deque
dR=[0,0,-1,1]
dC=[1,-1,0,0]
inf=9876543210

N,M=map(int,input().split())
L=[]
for i in range(N):
    L.append(list(map(int,list(input()))))

def bfs(sR,sC):
    # 방문안한것=0, 방문했는데 큰것=1, 방문했는데 똑같은것=2
    bfsV=[[0 for j in range(M)] for i in range(N)]

    bfsV[sR][sC]=2
    sH=L[sR][sC]
    q=deque([[sR,sC]])
    aroundH=inf #주변블럭 중 가장 낮은 블
    while(q):
        r,c=q.popleft()
        #print(r,c)
        for k in range(4):
            tempR=r+dR[k]
            tempC=c+dC[k]
            if 0<=tempR<N and 0<=tempC<M:
                if bfsV[tempR][tempC]==0:
                    if L[tempR][tempC]==sH:
                        q.append([tempR,tempC])
                        bfsV[tempR][tempC]=2
                    elif L[tempR][tempC]>sH:
                        if L[tempR][tempC]<aroundH:
                            aroundH=L[tempR][tempC]
                        bfsV[tempR][tempC]=1
                    else:
                        return 0
            else:
                return 0

    added=aroundH-sH
    count=0
    for i in range(1,N-1):
        for j in range(1,M-1):
            if bfsV[i][j]==2:
                L[i][j]=aroundH
                count+=1
    return count*added

ans=0
# 제일 낮은블럭 찾기
while(1):
    isUpdate=False
    visited=[[0 for j in range(M)] for i in range(N)]
    for i in range(1,N-1):
        for j in range(1,M-1):
            if not visited[i][j]:
                #print(i,j,"는")
                temp=bfs(i,j)
                if temp!=0:
                    isUpdate=True
                    ans+=temp

    if not isUpdate:
        break
print(ans)



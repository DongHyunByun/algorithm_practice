from itertools import combinations
from collections import deque

maxNum=9876543210
dR=[0,0,-1,1]
dC=[1,-1,0,0]

def main():
    N,M=map(int,input().split())
    L=[]
    for i in range(N):
        L.append(list(map(int,input().split())))
    #바이러스 가능지점찾기
    virus=[]
    for i in range(N):
        for j in range(N):
            if L[i][j]==2:
                virus.append([i,j])
    virusCom=list(combinations(virus,M))

    ans=maxNum
    #각케이스별 시행
    for viruses in virusCom:
        time=0
        #맵 만들기
        nowMap=[[0 for j in range(N)] for i in range(N)]
        for i in range(N):
            for j in range(N):
                # 활성바이러스이면?
                if [i,j] in viruses:
                    nowMap[i][j]=0
                # 벽이면?
                elif L[i][j]==1:
                    nowMap[i][j]="-"
                # 비활성바이러스이면?
                elif L[i][j]==2:
                    nowMap[i][j]="*"
                # 빈곳이면?
                elif L[i][j]==0:
                    nowMap[i][j]=-1

        #큐시작
        q=deque([viruses[i] for i in range(M)])
        while(q):
            temp=q.popleft()
            r=temp[0]
            c=temp[1]
            if nowMap[r][c]>ans:
                break
            for k in range(4):
                tempR=r+dR[k]
                tempC=c+dC[k]
                # 빈곳이거나 비활성이면 확장
                if 0<=tempR<N and 0<=tempC<N and nowMap[tempR][tempC] in [-1,"*"]:
                    if nowMap[tempR][tempC]==-1:
                        time=nowMap[r][c] + 1
                    nowMap[tempR][tempC] = nowMap[r][c] + 1
                    q.append([tempR,tempC])
        #바이러스 다 퍼졌는지 검사
        isSpread=True
        for i in range(N):
            for j in range(N):
                if nowMap[i][j]==-1:
                    isSpread=False
                    break

        if isSpread:
            if time<ans:
                ans=time

    if ans==maxNum:
        print(-1)
    else:
        print(ans)

main()
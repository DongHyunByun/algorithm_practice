from copy import deepcopy
from itertools import combinations
from collections import deque

N,M,D=map(int,input().split())
L=[]
dR=[0,-1,0]
dC=[-1,0,1]
for i in range(N):
    L.append(list(map(int,input().split())))

def attack(arches,copiedL):
    global nowAns
    # 궁수3명 죽일대상 선정
    kill = []
    for archCol in arches:
        visited=[[-1 for j in range(M)] for i in range(N)]
        q=deque([[N-1,archCol]])
        #바로처음에 있으면?
        if copiedL[N-1][archCol]==1:
            if [N-1,archCol] not in kill:
                kill.append([N-1,archCol])
            continue
        visited[N-1][archCol]=1
        while(q):
            temp=q.popleft()
            r=temp[0]
            c=temp[1]
            #해당위치 적있다면?
            if copiedL[r][c]==1:
                if [r,c] not in kill:
                    kill.append([r,c])
                break
            for k in range(3):
                tempR=r+dR[k]
                tempC=c+dC[k]
                if 0<=tempR<N and 0<=tempC<M and visited[tempR][tempC]==-1 and visited[r][c]<D:
                    visited[tempR][tempC]=visited[r][c]+1
                    q.append([tempR,tempC])
    # 죽이기
    for r,c in kill:
        copiedL[r][c]=0
    return len(kill)


def main():
    forCom=[i for i in range(M)]
    combi=list(combinations(forCom,3))
    ans=0
    #케이스 시작
    for arches in combi:
        #print("케이스시작",arches)
        nowAns=0
        copiedL=deepcopy(L)
        #총 N번 내려감
        for down in range(N):
            '''
            print(down+1,"번째 적군상태")
            for r in range(N):
                print(copiedL[r])
            '''
            #궁수공격
            nowAns+=attack(arches,copiedL)
            #적이동
            copiedL.pop()
            copiedL.insert(0,[0 for _ in range(M)])
        #print(nowAns,"명죽임!")
        if nowAns>ans:
            ans=nowAns
    print(ans)

main()
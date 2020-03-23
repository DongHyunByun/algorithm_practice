from copy import deepcopy
from itertools import combinations

N,M,D=map(int,input().split())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))

def attack(arches,copiedL):
    #세궁수 ㄱㄱ
    toKill = []
    for archCol in arches:
        isKill=False
        #가까운 거리부터 시작
        for i in range(D):
            # 첫칸
            r=N-1
            c=archCol-i
            if c>=0 and copiedL[r][c]==1:
                if [r,c] not in toKill:
                    toKill.append([r,c])
                isKill=True
                break
            # 왼쪽칸
            for j in range(i):
                r-=1
                c+=1
                if 0<=r<N and 0<=c<M :
                    if copiedL[r][c] == 1:
                        if [r, c] not in toKill:
                            toKill.append([r, c])
                        isKill=True
                        break
                else:
                    continue
            if isKill:
                break
            # 오른쪽칸
            for j in range(i):
                r+=1
                c+=1
                if 0<=r<N and 0<=c<M :
                    if copiedL[r][c] == 1:
                        if [r, c] not in toKill:
                            toKill.append([r, c])
                        isKill=True
                        break
                else:
                    continue
            if isKill:
                break
    ans=0
    for r,c in toKill:
        copiedL[r][c]=0
        ans+=1
    return ans

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
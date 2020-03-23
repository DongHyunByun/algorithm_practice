from copy import deepcopy
L=list(map(int,input().split()))
#구역별 점수
myMap=[[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40],
       [10,13,16,19,25,30,35,40],
       [20,22,24,25,30,35,40],
       [30,28,27,26,25,30,35,40]]

def move(r,c,diceNum):
    c += diceNum
    if len(myMap[r])<=c:
        return -1,-1,0
    else:
        if r==0:
            if c==5:
                r=1
                c=0
            elif c==10:
                r=2
                c=0
            elif c==15:
                r=3
                c=0
            elif c==20:
                r=1
                c=7
        return r,c,myMap[r][c]

def dfs(horse,cnt,point):
    global ans
    #다움직임
    if (cnt==10):
        if point>ans:
            ans=point
        return
    #네말 모두 움직일수 없는지 확인
    impossible=True
    #네가지말에 각각 적용
    for i in range(4):
        r=horse[i][0]
        c=horse[i][1]

        # 이미끝난말이면 다음것
        if r==-1:
            continue

        tempR,tempC,tempPoint=move(r,c,L[cnt])
        #새로옮긴 위치가 끝이 아니면
        if tempR!=-1:
            isPossible = True
            #이미 말이있으면 못감
            #같은경로확인
            if [tempR,tempC] in horse:
                isPossible=False
                continue
            #다른경로확인
            if tempR==1 and tempC>=4:
                for j in range(4):
                    if horse[j] in [[2,tempC-1],[3,tempC]]:
                        isPossible=False
                        break
            elif tempR==2 and tempC>=3:
                for j in range(4):
                    if horse[j] in [[1,tempC+1],[3,tempC+1]]:
                        isPossible=False
                        break
            elif tempR==3 and tempC>=4:
                for j in range(4):
                    if horse[j] in [[2,tempC-1],[1,tempC]]:
                        isPossible=False
                        break
            #옮길수있으면 진행 아니면 다음말 이동
            if isPossible:
                impossible=False
            else:
                continue
        #끝이면
        else:
            impossible=False
        horse[i][0]=tempR
        horse[i][1]=tempC
        dfs(horse,cnt+1,point+tempPoint)
        horse[i][0]=r
        horse[i][1]=c

    #옮길말 없으면 현재값에서 확인
    if impossible:
        if point>ans:
            ans=point

ans=0
dfs([[0,0],[0,0],[0,0],[0,0]],0,0)
print(ans)
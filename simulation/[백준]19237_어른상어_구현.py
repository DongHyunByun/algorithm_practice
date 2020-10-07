N,M,K=map(int,input().split())

dR=[0,-1,1,0,0]
dC=[0,0,0,-1,1]

# 상어위치
L=[]
def intMinus(a):
    return int(a)-1
for i in range(N):
    L.append(list(map(intMinus,input().split())))

# 냄새 smell[i][j]=[a,b] : a상어남긴 b초남은 냄
smell=[[0 for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        if L[i][j]!=-1:
            smell[i][j]=[L[i][j],K]

# 상어 초기 방향
to=list(map(int,input().split()))

# loc[i]=[행,렬,방향] : i번째 상어의 행,렬,방향
loc= {}
for i in range(N):
    for j in range(N):
        if L[i][j]!=-1:
            loc[L[i][j]]=[i,j,to[L[i][j]]]

# 상어별 방향규칙 dRule[a][t]=[1,2,3,4] : a상어의 t방향일때  우선순위는 1,2,3,4 순
dRule=[]
for i in range(M):
    tempS=[0]
    for j in range(4):
        temp=list(map(int,input().split()))
        tempS.append(temp)
    dRule.append(tempS)

def move(num,r,c,d):
    # 비어있는지 확인
    for k in dRule[num][d]:
        tempR=r+dR[k]
        tempC=c+dC[k]
        if 0<=tempR<N and 0<=tempC<N and smell[tempR][tempC]==0:
            return tempR,tempC,k
    # 자기냄새로
    for k in dRule[num][d]:
        tempR=r+dR[k]
        tempC=c+dC[k]
        if 0 <= tempR < N and 0 <= tempC < N and smell[tempR][tempC][0]==num:
            return tempR,tempC,k

time=1
while(1):
    # 상어 이동
    #print(loc)
    for i in loc:
        r,c,d=loc[i]
        tempR,tempC,d=move(i,r,c,d)
        loc[i]=[tempR,tempC,d]
    '''
    print("이동후")
    print(loc)
    '''

    # 겹치는 상어 확인
    tempL=[[-1 for j in range(N)] for i in range(N)]
    delL=[]
    for i in loc:
        r=loc[i][0]
        c=loc[i][1]
        # 겹치면?
        if tempL[r][c]!=-1:
            if i<tempL[r][c]:
                delL.append(tempL[r][c])
                tempL[r][c]=i
            else:
                delL.append(i)
        else:
            tempL[r][c]=i
    # 겹치는 상어 삭제
    #print("지울것들",delL)
    for delNum in delL:
        del loc[delNum]
    '''
    print("현재상어들 위치")
    print(loc)
    '''

    # 시간경과
    for i in range(N):
        for j in range(N):
            if smell[i][j]!=0:
                smell[i][j][1]-=1
                if smell[i][j][1]==0:
                    smell[i][j]=0
    '''
    print("시간경과")
    for i in smell:
        print(i)
    '''

    # 현재 상어들 위치 반영
    for num in loc:
        r,c,d=loc[num]
        smell[r][c]=[num,K]

    '''
    print("최종 냄새")
    for i in smell:
        print(i)
    '''

    if len(loc)==1:
        break

    time+=1
    if time==1001:
        break

if time==1001:
    print(-1)
else:
    print(time)
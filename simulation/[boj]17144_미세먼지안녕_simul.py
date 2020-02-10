from collections import deque

R,C,T=map(int,input().split())
L=[]
dR=[0,0,-1,1]
dC=[-1,1,0,0]

dU=[[0,1],[-1,0],[0,-1],[1,0]]
dD=[[0,1],[1,0],[0,-1],[-1,0]]

for i in range(R):
    L.append(list(map(int,input().split())))
for i in range(R):
    for j in range(C):
        L[i][j]=[L[i][j]]

# 공기청정기 위치
for i in range(R):
    if L[i][0][0]==-1:
        upC=i
        downC=i+1
        break

for t in range(T):
    # 확산
    for i in range(R):
        for j in range(C):
            if L[i][j][0]>0:
                cnt=0
                for k in range(4):
                    tempI=i+dR[k]
                    tempJ=j+dC[k]
                    if 0<=tempI<R and 0<=tempJ<C and L[tempI][tempJ][0]!=-1:
                        L[tempI][tempJ].append(L[i][j][0]//5)
                        cnt+=1
                L[i][j][0]-=(L[i][j][0]//5)*cnt
    # 합치기
    for i in range(R):
        for j in range(C):
            L[i][j]=[sum(L[i][j])]

    # 공기청정기작동
    #<윗부분>
    direct=0
    r=upC
    c=0
    q=deque([0])
    while(1):
        #print(direct,"현재위치",r,c)
        tempR=r+dU[direct][0]
        tempC=c+dU[direct][1]
        if tempR==upC and tempC==0:
            break
        if 0<=tempR<R and 0<=tempC<C:
            q.append(L[tempR][tempC][0])
            L[tempR][tempC][0]=q.popleft()
            r=tempR
            c=tempC
        else:
            direct+=1
            tempR=r+dU[direct][0]
            tempC=c+dU[direct][1]
            q.append(L[tempR][tempC][0])
            L[tempR][tempC][0]=q.popleft()
            r=tempR
            c=tempC
    #<윗부분>
    direct = 0
    r = downC
    c = 0
    q = deque([0])
    while (1):
        # print(direct,"현재위치",r,c)
        tempR = r + dD[direct][0]
        tempC = c + dD[direct][1]
        if tempR == downC and tempC == 0:
            break
        if 0 <= tempR < R and 0 <= tempC < C:
            q.append(L[tempR][tempC][0])
            L[tempR][tempC][0] = q.popleft()
            r = tempR
            c = tempC
        else:
            direct += 1
            tempR = r + dD[direct][0]
            tempC = c + dD[direct][1]
            q.append(L[tempR][tempC][0])
            L[tempR][tempC][0] = q.popleft()
            r = tempR
            c = tempC

ans=0
for i in range(R):
    for j in range(C):
        ans+=L[i][j][0]
print(ans+2)

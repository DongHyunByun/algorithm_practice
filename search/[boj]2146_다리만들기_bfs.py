from collections import deque
dR=[0,0,-1,1]
dC=[1,-1,0,0]
maxNum=201
N=int(input())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))

# 구역설정
myMap=[[0 for i in range(N)] for j in range(N)]
isNum=1
for i in range(N):
    for j in range(N):
        if myMap[i][j]==0 and L[i][j]==1:
            q=deque([[i,j]])
            myMap[i][j]=isNum
            while(q):
                temp=q.popleft()
                r=temp[0]
                c=temp[1]
                for k in range(4):
                    tempR=r+dR[k]
                    tempC=c+dC[k]
                    if 0<=tempR<N and 0<=tempC<N and myMap[tempR][tempC]==0 and L[tempR][tempC]==1:
                        myMap[tempR][tempC]=isNum
                        q.append([tempR,tempC])
            isNum+=1
isNum-=1

#거리찾기
ans=maxNum
for i in range(N):
    for j in range(N):
        #(i,j)에서 각 섬까지의 최소거리
        if myMap[i][j]!=0:
            isDist=[maxNum for _ in range(isNum)]
            isDist[myMap[i][j]-1]=maxNum+1
            #다 찾으면 종료
            cnt=1
            visited=[[-1 for _ in range(N)] for _ in range(N)]
            q=deque([[i,j]])
            visited[i][j]=0
            while(q):
                temp=q.popleft()
                r=temp[0]
                c=temp[1]
                for k in range(4):
                    tempR=r+dR[k]
                    tempC=c+dC[k]
                    if 0<=tempR<N and 0<=tempC<N and visited[tempR][tempC]==-1 and myMap[tempR][tempC]!=myMap[i][j]:
                        # 섬이면?
                        if myMap[tempR][tempC]!=0:
                            if isDist[myMap[tempR][tempC]-1]==maxNum:
                                isDist[myMap[tempR][tempC]-1]=visited[r][c]
                                cnt+=1
                        # 섬아니면
                        else:
                            visited[tempR][tempC]=visited[r][c]+1
                            q.append([tempR,tempC])
                if cnt==isNum:
                    break
            #print(i,j,isDist)
            nowMin=min(isDist)
            if nowMin<ans:
                ans=nowMin
print(ans)
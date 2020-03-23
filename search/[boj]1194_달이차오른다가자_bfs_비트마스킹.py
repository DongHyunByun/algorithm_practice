from collections import deque
dR=[0,0,-1,1]
dC=[1,-1,0,0]


#입력받기
N,M=map(int,input().split())
L=[]
for i in range(N):
    L.append(list(input()))
#시작점, 끝점찾기
srt=[0,0]
fin=[0,0]
for i in range(N):
    for j in range(M):
        if L[i][j]=="0":
            srt[0]=i
            srt[1]=j
        elif L[i][j]=="1":
            fin[0]=i
            fin[1]=j
ans=-1
#큐시작
visited=[[[-1 for key in range(64)] for j in range(M)] for i in range(N)]
visited[srt[0]][srt[1]][0]=0
q=deque([[srt[0],srt[1],0]])
while(q):
    isFind=False
    r,c,key=q.popleft()
    binKey=bin(key)[2:]
    binKey=binKey.zfill(6)
    for k in range(4):
        tempR=r+dR[k]
        tempC=c+dC[k]
        if 0<=tempR<N and 0<=tempC<M and visited[tempR][tempC][key]==-1:
            #빈곳
            if L[tempR][tempC]==".":
                visited[tempR][tempC][key]=visited[r][c][key]+1
                q.append([tempR,tempC,key])
            #벽
            elif L[tempR][tempC]=="#":
                continue
            #열쇠
            elif 97<=ord(L[tempR][tempC])<=102:
                visited[tempR][tempC][key]=visited[r][c][key]+1
                #추가되는 키의 인덱스
                addedKeyIndx=ord(L[tempR][tempC])-97
                keyL=list(binKey)
                keyL[addedKeyIndx]="1"
                temp=int("".join(keyL))
                tempKey=int("0b"+str(temp),2)
                visited[tempR][tempC][tempKey]=visited[r][c][key]+1
                q.append([tempR,tempC,tempKey])
            #문
            elif 65<=ord(L[tempR][tempC])<=70:
                doorIndx=ord(L[tempR][tempC])-65
                if int(binKey[doorIndx]):
                    visited[tempR][tempC][key] = visited[r][c][key] + 1
                    q.append([tempR,tempC,key])
            #출발지(다른열쇠획득후겠지?)
            elif L[tempR][tempC]=="0":
                visited[tempR][tempC][key] = visited[r][c][key] + 1
                q.append([tempR, tempC, key])
            #도착
            else:
                ans=visited[r][c][key]+1
                isFind=True
    if isFind:
        break
print(ans)
from collections import deque
turn=[1,0]
dR=[0,1,-1,0]
dC=[1,0,0,-1]
dRR=[-1,-1,-1,0,0,1,1,1]
dCC=[-1,0,1,-1,1,-1,0,1]
N=int(input())
L=[]
for i in range(N):
    L.append(list(input()))

def move(a,b,c,dic):
    for k in range(4):
        tempA=[a[0]+dR[k],a[1]+dC[k]]
        tempB=[b[0]+dR[k],b[1]+dC[k]]
        tempC=[c[0]+dR[k],c[1]+dC[k]]
        if 0<=tempA[0]<N and 0<=tempA[1]<N and 0<=tempB[0]<N and 0<=tempB[1]<N and 0<=tempC[0]<N and 0<=tempC[1]<N and L[tempA[0]][tempA[1]]!="1" and L[tempB[0]][tempB[1]]!="1" and L[tempC[0]][tempC[1]]!="1" and visited[tempB[0]][tempB[1]][dic]==-1:
            visited[tempB[0]][tempB[1]][dic]=visited[b[0]][b[1]][dic]+1
            q.append([tempB[0],tempB[1],dic])
def rotate(b,dic):
    #방문되었는지 확인
    if visited[b[0]][b[1]][turn[dic]]!=-1:
        return
    #돌릴자리 있는지 확인
    r=b[0]
    c=b[1]
    for k in range(8):
        tempR=r+dRR[k]
        tempC=c+dCC[k]
        if tempR>=N or tempR<0 or tempC>=N or tempC<0 or L[tempR][tempC]=="1":
            return
    #방문안됐고, 돌릴자리있으면
    visited[r][c][turn[dic]]=visited[r][c][dic]+1
    q.append([r,c,turn[dic]])

#시작점찾기
isFind=False
for i in range(N):
    for j in range(N):
        if L[i][j]=="B":
            isFind=True
            tempI=i+dR[0]
            tempJ=j+dC[0]
            if 0<=tempI<N and 0<=tempJ<N and L[tempI][tempJ]=="B":
                srtR = tempI
                srtC = tempJ
                srtL = 0
            else:
                srtR = i+dR[1]
                srtC = j+dC[1]
                srtL = 1
            break
    if isFind:
        break

#끝지점찾기
isFind=False
for i in range(N):
    for j in range(N):
        if L[i][j]=="E":
            isFind=True
            tempI=i+dR[0]
            tempJ=j+dC[0]
            if 0<=tempI<N and 0<=tempJ<N and L[tempI][tempJ]=="E":
                finR = tempI
                finC = tempJ
                finL = 0
            else:
                finR = i+dR[1]
                finC = j+dC[1]
                finL = 1
            break
    if isFind:
        break

ans=0
visited=[[[-1,-1] for j in range(N)] for i in range(N)]
visited[srtR][srtC][srtL]=0
q=deque([[srtR,srtC,srtL]])
while(q):
    r,c,l=q.popleft()
    if [r,c,l]==[finR,finC,finL]:
        ans=visited[r][c][l]
        break

    #가로일때
    if l==0:
        x=[r,c-1]
        y=[r,c]
        z=[r,c+1]
        #print(x,y,z)
        move(x,y,z,l)
        rotate(y,l)
    #세로일때
    else:
        x=[r-1,c]
        y=[r,c]
        z=[r+1,c]
        #print(x, y, z)
        move(x,y,z,l)
        rotate(y,l)
    '''
    for i in visited:
        print(i)
    '''
print(ans)
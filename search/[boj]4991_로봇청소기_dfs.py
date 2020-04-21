from collections import deque
dR=[0,0,-1,1]
dC=[-1,1,0,0]

#map에 먼지 있으면 True
def isDirt(map):
    for i in range(h):
        for j in range(w):
            if map[i][j]=="*":
                return True
    return False

def bfs(startR,startC,nowMap,visited,dirtL):
    q = deque([[startR, startC]])
    while(q):
        r,c=q.popleft()
        for k in range(4):
            tempR=r+dR[k]
            tempC=c+dC[k]
            if 0<=tempR<h and 0<=tempC<w and visited[tempR][tempC]==-1:
                #깨끗한칸
                if nowMap[tempR][tempC]==".":
                    q.append([tempR,tempC])
                    visited[tempR][tempC]=visited[r][c]+1
                #더러운칸
                elif nowMap[tempR][tempC]=="*":
                    dirtL.append([tempR,tempC])
                    q.append([tempR,tempC])
                    visited[tempR][tempC]=visited[r][c]+1

def dfs(r,c,nowMap,cnt):
    #print(r,c)
    global ans
    if cnt>=ans:
        return True
    visited = [[-1 for j in range(w)] for i in range(h)]
    visited[r][c] = 0
    dirtL=[] #먼지위치저장
    bfs(r,c,nowMap,visited,dirtL)
    if dirtL:
        for i,j in dirtL:
            nowMap[i][j]="."
            if dfs(i,j,nowMap,cnt+visited[i][j]):
                nowMap[i][j] = "*"
            else:
                return False
        return True
    else:
        #먼지있으면
        if isDirt(nowMap):
            return False
        else:
            if ans>cnt:
                ans=cnt
            return True

while(1):
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    L=[]
    for i in range(h):
        temp=list(input())
        if "o" in temp:
            sR=i
            sC=temp.index("o")
        L.append(temp)
    ans=9876543210
    L[sR][sC]="."
    if dfs(sR,sC,L,0):
        print(ans)
    else:
        print(-1)
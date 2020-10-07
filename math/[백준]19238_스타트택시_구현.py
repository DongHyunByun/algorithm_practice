from collections import deque
dR=[0,0,-1,1]
dC=[1,-1,0,0]
INF=9876543210

N,M,oil=map(int,input().split())
L=[]
for i in range(N):
    L.append(list(map(int,input().split())))
sR,sC=map(int,input().split())
sR-=1
sC-=1
myMap=[[[] for j in range(N)] for i in range(N)]
for i in range(1,M+1):
    a,b,c,d=map(int,input().split())
    myMap[a-1][b-1].append(i) #출발지
    myMap[c-1][d-1].append(-i) #도착지


# 시작위치,남은연료 => 가장 가까운 출발지, 쓴연
def findShort(startR,startC,oil):
    for s in myMap[startR][startC]:
        if s>0:
            return startR,startC,s,0

    candi=[] #출발지 후
    d=INF
    visited=[[-1 for j in range(N)] for i in range(N)]
    q=deque([[startR,startC]])
    visited[startR][startC]=0

    while(q):
        r,c=q.popleft()
        # 기름이 다됐거나, 찾았으면
        if visited[r][c]==oil or visited[r][c]==d:
            continue
        for k in range(4):
            tempR=r+dR[k]
            tempC=c+dC[k]
            if 0<=tempR<N and 0<=tempC<N and visited[tempR][tempC]==-1 and L[tempR][tempC]==0:
                visited[tempR][tempC]=visited[r][c]+1
                q.append([tempR,tempC])
                for s in myMap[tempR][tempC]:
                    if s>0:
                        d=visited[tempR][tempC]
                        candi.append([tempR,tempC,s])

    candi.sort()
    if candi:
        return candi[0][0],candi[0][1],candi[0][2],d
    else:
        return -1,-1,-1,-1

#도착지 찾기
def findFin(startR,startC,oil,num):
    visited=[[-1 for j in range(N)] for i in range(N)]
    q=deque([[startR,startC]])
    visited[startR][startC]=0

    while(q):
        r,c=q.popleft()
        if visited[r][c]==oil:
            continue
        for k in range(4):
            tempR=r+dR[k]
            tempC=c+dC[k]
            if 0<=tempR<N and 0<=tempC<N and visited[tempR][tempC]==-1 and L[tempR][tempC]==0:
                for f in myMap[tempR][tempC]:
                    if f==-num:
                        return tempR,tempC,f,visited[r][c]+1
                visited[tempR][tempC]=visited[r][c]+1
                q.append([tempR,tempC])

    return -1,-1,-1,-1




for _ in range(M):
    #print(_ + 1, "번째 현재위치",sR,sC,oil)
    newR,newC,type,move=findShort(sR,sC,oil)
    #print("이동후",newR,newC,"움직임",move)

    # 출발지까지 못가면
    if newR==-1:
        oil=-1
        break
    else:
        myMap[newR][newC].remove(type)
        oil-=move
        #print(type,"찾기")
        sR,sC,type,move=findFin(newR,newC,oil,type)
        #print("도착지",sR,sC,"움직임",move)
        if sR==-1:
            oil=-1
            break
        else:
            myMap[sR][sC].remove(type)
            oil+=move
            '''
            print("도착지 도착후 기름",oil)
            for i in myMap:
                print(i)
            print("---------------------")
            '''
print(oil)


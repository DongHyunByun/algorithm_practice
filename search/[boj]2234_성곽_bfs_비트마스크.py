from collections import deque
dR=[1,0,-1,0]
dC=[0,1,0,-1]
N,M=map(int,input().split())
L=[]

def toBin(a):
    return bin(int(a))[2:].zfill(4)
def searchFirst():
    cnt=0
    maxSize=0
    for i in range(M):
        for j in range(N):
            if visited[i][j]==-1:
                cnt+=1
                size=1
                q=deque([[i,j]])
                visited[i][j]=cnt
                while(q):
                    r,c=q.popleft()
                    for k in range(4):
                        tempR=r+dR[k]
                        tempC=c+dC[k]
                        if 0<=tempR<M and 0<=tempC<N and visited[tempR][tempC]==-1 and L[r][c][k]=="0":
                            q.append([tempR,tempC])
                            visited[tempR][tempC]=cnt
                            size+=1
                if size>maxSize:
                    maxSize=size

    print(cnt)
    print(maxSize)
def open(i,j,k):
    temp = list(L[i][j])
    temp[k] = "0"
    L[i][j]="".join(temp)

def close(i,j,k):
    temp=list(L[i][j])
    temp[k]="1"
    L[i][j]="".join(temp)

def searchBreak():
    maxSize=0
    for i in range(M):
        for j in range(N):
            for k in range(4):
                if int(L[i][j][k]):
                    open(i,j,k)
                    size = 1
                    visited = [[-1 for x in range(N)] for y in range(M)]
                    q=deque([[i,j]])
                    visited[i][j] = 1
                    while(q):
                        r,c=q.popleft()
                        for l in range(4):
                            tempR=r+dR[l]
                            tempC=c+dC[l]
                            if 0<=tempR<M and 0<=tempC<N and visited[tempR][tempC]==-1 and L[r][c][l]=="0":
                                q.append([tempR,tempC])
                                visited[tempR][tempC]=1
                                size+=1
                    if size>maxSize:
                        maxSize=size
                    close(i,j,k)
    print(maxSize)

for i in range(M):
    L.append(list(map(toBin,input().split())))

visited=[[-1 for j in range(N)] for i in range(M)]
searchFirst()
searchBreak()

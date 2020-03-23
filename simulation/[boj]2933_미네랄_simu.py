from collections import deque

dR=[0,0,-1,1]
dC=[1,-1,0,0]
R,C=map(int,input().split())
L=[]
for i in range(R):
    L.append(list(input()))
N=int(input())
stick=list(map(int,input().split()))

# side가 0이면 왼쪽, 1이면 오른쪽
def throw(side,high):
    if side==0:
        for j in range(C):
            if L[R-high][j]=="x":
                L[R-high][j]="."
                return
    else:
        for j in range(C-1,-1,-1):
            if L[R-high][j]=="x":
                L[R-high][j]="."
                return

def find():
    #떠있는 클러스터 찾기
    for j in range(C):
        if L[R-1][j]=="x" and visited[R-1][j]==-1:
            q=deque([[R-1,j]])
            visited[R-1][j]=1
            while(q):
                r,c=q.popleft()
                for k in range(4):
                    tempR=r+dR[k]
                    tempC=c+dC[k]
                    if 0<=tempR<R and 0<=tempC<C and L[tempR][tempC]=="x" and visited[tempR][tempC]==-1:
                        visited[tempR][tempC]=1
                        q.append([tempR,tempC])

    #아래끝찾기
    isCluster=False
    lowerBound=[-1 for j in range(C)]
    for i in range(R):
        for j in range(C):
            if visited[i][j]==-1 and L[i][j]=="x":
                isCluster=True
                lowerBound[j]=i
                visited[i][j]=2
    return isCluster

def down():
    downNum=101
    for i in range(R):
        for j in range(C):
            if visited[i][j]==2:
                for k in range(1,R):
                    tempR=i+k
                    if 0<=tempR<R:
                        if visited[tempR][j]==2:
                            break
                        elif visited[tempR][j]==1:
                            if k-1<downNum:
                                downNum=k-1
                                break
                        else:
                            continue
                    else:
                        if k-1<downNum:
                            downNum=k-1
                            break
    newvisited=[[-1 for j in range(C)] for i in range(R)]
    for i in range(R):
        for j in range(C):
            if visited[i][j]==2:
                newvisited[i+downNum][j]=2
    for i in range(R):
        for j in range(C):
            if visited[i][j]==2:
                L[i][j]="."
            if newvisited[i][j]==2:
                L[i][j]="x"





for i in range(N):
    #print(i, "번쨰!")
    #던지기
    throw(i%2,stick[i])
    #클러스터찾기
    visited = [[-1 for j in range(C)] for i in range(R)]
    if find():
        down()
    '''
    for x in visited:
        print(x)
    '''
for i in range(R):
    print("".join(L[i]))
from collections import deque
import sys

dR=[0,0,-1,1]
dC=[1,-1,0,0]

N=int(input())
L=[[[0,0] for j in range(2*N)] for i in range(N)]

def findLoc(r,c):
    if (r%2+c%2)%2==0:
        return c,c+1
    else:
        return c-1,c

def findRoute(r,c):
    index=L[r][c][1]
    route.appendleft(index)

    if index==1:
        return

    nextR,nextC=visited[r][c]
    findRoute(nextR,nextC)


r=0
c=0
for i in range(N*N-N//2):
    a,b=map(int,input().split())
    L[r][c]=a,i+1
    L[r][c+1]=b,i+1

    c+=2
    if c>=2*N-1:
        r+=1
        if r%2==0:
            c=0
        else:
            c=1


q=deque([[0,0],[0,1]])
visited=[[[] for j in range(2*N)] for i in range(N)]
visited[0][0]=[0,0]
visited[0][1]=[0,1]

while(q):
    r,c=q.popleft()
    for k in range(4):
        tempR=r+dR[k]
        tempC=c+dC[k]
        if 0<=tempR<N and 0<=tempC<2*N and visited[tempR][tempC]==[] and L[r][c][0]==L[tempR][tempC][0]:
            tempLeftC,tempRightC=findLoc(tempR,tempC)
            visited[tempR][tempLeftC] = [r,c]
            visited[tempR][tempRightC] = [r,c]
            q.append([tempR,tempLeftC])
            q.append([tempR, tempRightC])

'''
for i in visited:
    print(i)
'''

route=deque([])
for i in range(N-1,-1,-1):
    for j in range(2*N-1,-1,-1):
        if visited[i][j]!=[]:
            findRoute(i,j)
            print(len(route))
            print(*route)
            sys.exit()


